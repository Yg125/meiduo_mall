from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^register/', views.Register.as_view()),
    re_path(r'^usernames/(?P<username>\w{5,20})/count/$', views.CheckUsernameView.as_view()),
]
