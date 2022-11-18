from django.db import models
from django.contrib.auth.models import AbstractUser


# 1,定义用户模型类
class User(AbstractUser):
    # 1, 增加额外的属性
    mobile = models.CharField(verbose_name="手机号", max_length=11, unique=True)

    # 2, 指定表名信息
    class Meta:
        db_table = "tb_users"
