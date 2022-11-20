import re

from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.views import View
from .models import User


class Register(View):
    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        # 1. 获取参数
        username = request.POST.get('user_name')
        pwd = request.POST.get('pwd')
        cpwd = request.POST.get('cpwd')
        phone = request.POST.get('phone')
        msg_code = request.POST.get('msg_code')
        allow = request.POST.get('allow')
        # 2. 校验参数
        # 为空校验
        if not all([username, pwd, cpwd, phone, msg_code, allow]):
            return HttpResponseForbidden('参数不全')
        # 密码校验
        if pwd != cpwd:
            return HttpResponseForbidden('密码输入不正确')
        # 手机号格式校验
        if not re.match(r'^1[3-9]\d{9}$', phone):
            return HttpResponseForbidden("手机号格式有误")
        # 短信验证码校验

        # 同意校验
        if allow != 'on':
            return HttpResponseForbidden('协议需要同意')
        # 3. 数据入库
        User.objects.create(username=username, password=pwd, mobile=phone)
        user = User.objects.get(username=username)
        user.set_password(pwd)
        user.save()
        # 4. 返回响应
        return redirect('http://www.taobao.com')


# 2, 判断用户名是否存在
class CheckUsernameView(View):
    def get(self, request, username):
        # 1, 根据用户名查询用户数量
        count = User.objects.filter(username=username).count()

        # 2, 返回响应
        return JsonResponse({"count": count, "code": 0})


# 2, 判断手机号是否存在
class CheckMobileView(View):
    def get(self, request, mobile):
        # 1, 根据用户名查询用户数量
        count = User.objects.filter(mobile=mobile).count()

        # 2, 返回响应
        return JsonResponse({"count": count, "code": 0})


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self,request):

        # 1  获取参数
        username = request.POST.get('username')
        pwd = request.POST.get('pwd')
        remembered = request.POST.get('remembered')

        # 2,校验参数
        # 2,1 为空校验
        if not all([username, pwd]):
            return HttpResponseForbidden("参数不全")

        # 2,2 用户名格式
        if not re.match(r'^[a-zA-Z0-9_-]{5,20}$', username):
            return HttpResponseForbidden("用户名格式不对")

        # 2,3 密码格式校验ß
        if not re.match(r'^[0-9A-Za-z]{8,20}$', pwd):
            return HttpResponseForbidden("密码格式不对")

        # 2,4 账号密码正确性校验, 如果认证成功返回用户对象, 不成功返回None
        user = authenticate(request, username=username, password=pwd)

        if not user:
            return HttpResponseForbidden("账号或者密码不正确")

        if not user:
            return HttpResponse('账户密码不正确')

        #3 数据入库

        login(request, user)        # 就是将用户的信息存储在session
        if remembered == "on":
            request.session.set_expiry(3600*24*2)
        else:
            request.session.set_expiry(0)
        #4 返回响应

        return redirect('/')
