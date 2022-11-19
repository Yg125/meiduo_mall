import random
import re

import redis
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views import View
from django_redis import get_redis_connection

from libs.captcha.captcha import captcha


class ImageCodeView(View):
    def get(self, request, uuid):
        # 1 获取图片验证码，图片
        _, text, image_data = captcha.generate_captcha()
        # 2 存储图片验证码于redis
        redis_conn = get_redis_connection("code")
        redis_conn.set('image_code_%s' % uuid, text, 60)
        # 3返回响应
        return HttpResponse(image_data, content_type='image/jpg')


class SMSCodeView(View):
    def get(self, request, mobile):
        # 1,获取参数
        image_code = request.GET.get("image_code")
        image_code_id = request.GET.get("image_code_id")
        # 2,校验参数
        # 2,1 为空检验
        if not all([image_code, image_code_id]):
            return JsonResponse({"code": 4001, "errmsg": "参数不全"})

        # 2,1 手机号格式
        if not re.match(r'^1[3-9]\d{9}$', mobile):
            return JsonResponse({"code": 4001, "errmsg": "手机号格式有误"})

        # 2,2 图片验证码正确性
        redis_conn = get_redis_connection("code")
        redis_image_code = redis_conn.get("image_code_%s" % image_code_id)

        if image_code != redis_image_code.decode():
            return JsonResponse({"code": 4001, "errmsg": "图片验证码错误"})

        # 3,发送短信,数据入库
        sms_code = "%06d" % random.randint(0, 999999)  # 生成随机六位数
        print("sms_code = %s" % sms_code)

        # 4,返回响应
        return JsonResponse({"code": 0})
