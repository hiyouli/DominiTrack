# domains/tasks.py

from celery import shared_task
from django.utils import timezone
from .models import Domain
from .whois_lookup import get_domain_expiration_date
import logging

logger = logging.getLogger(__name__)

@shared_task
def update_domain_expiration_date(domain_id):
    """
    通过 WHOIS 查询更新单个域名的到期日期。
    """
    try:
        domain = Domain.objects.get(id=domain_id)
        if not domain.auto_lookup_enabled:
            logger.info(f"Auto-lookup disabled for domain {domain.name}. Skipping.")
            return

        logger.info(f"Starting WHOIS lookup for domain: {domain.name}")
        new_expiration_date = get_domain_expiration_date(domain.name)

        if new_expiration_date:
            if new_expiration_date != domain.expiration_date:
                domain.expiration_date = new_expiration_date
                domain.last_lookup_date = timezone.now()
                domain.save()
                logger.info(f"Updated expiration date for {domain.name} to {new_expiration_date}")
            else:
                domain.last_lookup_date = timezone.now()
                domain.save()
                logger.info(f"Expiration date for {domain.name} is the same: {new_expiration_date}")
        else:
            logger.warning(f"Could not retrieve new expiration date for {domain.name}")

    except Domain.DoesNotExist:
        logger.error(f"Domain with ID {domain_id} does not exist.")
    except Exception as e:
        logger.error(f"Error in update_domain_expiration_date for domain ID {domain_id}: {e}", exc_info=True)


@shared_task
def check_and_send_expiration_reminders():
    """
    检查所有域名并发送到期提醒。
    """
    logger.info("Starting check_and_send_expiration_reminders task.")
    domains = Domain.objects.all()
    for domain in domains:
        days_left = domain.days_until_expiration()
        domain_name = domain.name
        owner_email = domain.owner.email # 获取域名所有者的邮箱

        # 这里只是一个示例，您可以根据需要扩展提醒逻辑
        # 例如：设置多个提醒阈值，检查是否已发送过提醒，支持微信/TG等
        if owner_email and (days_left == 90 or days_left == 30 or days_left == 7 or days_left == 1):
            subject = f"DominiTrack: 您的域名 {domain_name} 即将到期！"
            message = (
                f"您的域名 {domain_name} 将在 {days_left} 天后 ({domain.expiration_date}) 到期。\n"
                f"请尽快前往您的注册商进行续费，以免造成不必要的损失！\n"
                f"当前状态: {domain.status}\n"
                f"链接: http://localhost:8080/domains (将来替换为您的实际网站地址)"
            )
            # 导入发送邮件的函数（此处简化，实际应封装）
            from django.core.mail import send_mail
            try:
                send_mail(
                    subject,
                    message,
                    'noreply@dominitrack.com', # 发件人邮箱，未来配置SMTP服务
                    [owner_email],
                    fail_silently=False,
                )
                logger.info(f"Sent email reminder for {domain_name} to {owner_email}. Days left: {days_left}")
            except Exception as e:
                logger.error(f"Failed to send email reminder for {domain_name} to {owner_email}: {e}")

        # TODO: 未来在这里添加微信、Telegram 等提醒逻辑
        # if days_left == XX and owner_has_wechat_configured:
        #    send_wechat_notification(...)
        # if days_left == YY and owner_has_telegram_configured:
        #    send_telegram_notification(...)

    logger.info("Finished check_and_send_expiration_reminders task.")

# 每日定时任务（在 Celery Beat 中配置）
# 示例：每24小时运行一次 check_and_send_expiration_reminders
# 实际配置会在 Celery Beat 启动时通过 settings.py 或命令行完成