"""
 项目数据库配置文件
"""
from drf_template.settings import BASE_DIR

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "*******",
        "PORT": "3306"
    },
    "built_in": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / 'db.sqlite3',
    }
}

# 将django内置的数据库模型放在built_in中
DATABASE_APPS_MAPPING = {
    "contenttypes": "built_in",
    "auth": "built_in",
    "admin": "built_in",
}
