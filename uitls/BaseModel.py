from django.db import models


class BaseModel(models.Model):
    '''
    基础模型，默认附带创建时间和修改时间两个字段,
    项目中所有的模型都会基于此模型
    '''
    created_time = models.DateTimeField(auto_now_add=True, blank=True, verbose_name="创建时间")
    modified_time = models.DateTimeField(auto_now=True, blank=True, verbose_name="修改时间")

    class Meta:
        abstract = True
