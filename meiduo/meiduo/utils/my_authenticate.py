from django.contrib.auth.backends import ModelBackend
import re
from apps.users.models import User


# 1, 重写系统认证方法
class MyModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):

        # 1, 根据username查询用户
        try:
            if re.match(r'^1[3-9]\d{9}$', username):
                user = User.objects.get(mobile=username)
            else:
                user = User.objects.get(username=username)
        except Exception as e:
            return None

        # 2, 校验密码
        if user.check_password(password):
            return user
        else:
            return None
