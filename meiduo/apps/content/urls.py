from django.conf.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.IndexView.as_view()),
    re_path(r'^logout/$',views.LogoutView.as_view())
]