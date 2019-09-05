from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser


config = {
    'title': 'API Document',
    'authentication_classes': [SessionAuthentication],
    'permission_classes': [IsAdminUser],
}
