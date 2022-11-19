import redis
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha


class ImageCodeView(View):
    def get(self, request, uuid):
        # 1 获取图片验证码，图片
        _, code, image_data = captcha.generate_captcha()
        # 2 存储图片验证码于redis
        redis_conn = get_redis_connection('code')
        redis_conn.set('image_code%s' % uuid, code, 60)
        # 3返回响应
        return HttpResponse(image_data, content_type='image/jpg')
