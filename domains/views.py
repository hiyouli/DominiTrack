# domains/views.py

from rest_framework import viewsets, permissions
from .models import Domain
from .serializers import DomainSerializer

class DomainViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows domains to be viewed or edited.
    """
    queryset = Domain.objects.all().order_by('expiration_date')
    serializer_class = DomainSerializer
    permission_classes = [permissions.IsAuthenticated] # 只允许认证用户访问

    def get_queryset(self):
        """
        Only allow users to see their own domains.
        """
        # 如果是管理员，可以看到所有域名
        if self.request.user.is_staff:
            return Domain.objects.all().order_by('expiration_date')
        # 否则，只看自己的域名
        return Domain.objects.filter(owner=self.request.user).order_by('expiration_date')

    def perform_create(self, serializer):
        """
        Set the owner of the domain to the current user when creating.
        """
        serializer.save(owner=self.request.user)