"""
项目日志配置文件
"""

from drf_template.settings import BASE_DIR

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,

    # 格式化器
    "formatters": {
        'verbose': {
            'format': '{levelname} {asctime} {module}{message}',
            'style': '{',
        },
        'simple': {
            'format': '{levelname} {message}',
            'style': '{',
        },
    },

    # 处理器
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': "{}/logs/django/info.log".format(BASE_DIR),
            'formatter': 'verbose',
            'maxBytes': 1024,
            'backupCount': 5,
            'encoding': 'utf-8',
        },

    },
    'loggers': {
        'django.request': {
            'handlers': ['file'],
            'level': 'INFO',
            'propagate': False,
        },
    }
}
