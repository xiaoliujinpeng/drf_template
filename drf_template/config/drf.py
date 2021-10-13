"""
Django Rest Framework 相关配置
"""
from datetime import timedelta

REST_FRAMEWORK = {
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'UNAUTHENTICATED_USER': None,
    'DEFAULT_RENDERER_CLASSES': ['utils.response.MyJsonRenderer', 'rest_framework.renderers.BrowsableAPIRenderer'],
    'DEFAULT_FILTER_BACKENDS': ['django_filters.rest_framework.DjangoFilterBackend'],
    'DEFAULT_AUTHENTICATION_CLASSES': [
            'rest_framework_simplejwt.authentication.JWTAuthentication',
        ],
}
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=1),
}