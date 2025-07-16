# domains/whois_lookup.py

import whois # 我们需要安装这个库
import datetime
import logging

logger = logging.getLogger(__name__)

def get_domain_expiration_date(domain_name):
    """
    通过 WHOIS 查询获取域名到期日期。
    """
    try:
        w = whois.whois(domain_name)
        # WHOIS 结果的日期字段名称可能因 TLD 和 WHOIS 服务器而异
        # 尝试常见的字段名
        expiration_date = w.expiration_date

        if isinstance(expiration_date, list):
            # 有些WHOIS服务器会返回日期列表，取第一个或最新的
            expiration_date = expiration_date[0]

        if isinstance(expiration_date, datetime.datetime):
            return expiration_date.date() # 只返回日期部分
        elif isinstance(expiration_date, datetime.date):
            return expiration_date
        else:
            logger.warning(f"WHOIS lookup for {domain_name}: Expiration date format not recognized: {expiration_date}")
            return None
    except Exception as e:
        logger.error(f"Error performing WHOIS lookup for {domain_name}: {e}")
        return None

if __name__ == '__main__':
    # 简单的测试
    test_domains = ["google.com", "example.com", "baidu.com", "nonexistentdomainxyz123.com"]
    for domain in test_domains:
        exp_date = get_domain_expiration_date(domain)
        if exp_date:
            print(f"Domain: {domain}, Expiration Date: {exp_date}")
        else:
            print(f"Could not retrieve expiration date for {domain}")