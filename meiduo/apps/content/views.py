from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.views import View


# 1, 展示首页
class IndexView(View):
    def get(self, request):
        return render(request, 'index.html')


class LogoutView(View):
    def get(self, request):
        # 1 清除session
        logout(request)  # 调用API清除session

        # 2 清除cookie
        response = redirect('/')
        response.delete_cookie("username")
        return response
