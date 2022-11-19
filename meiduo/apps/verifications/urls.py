from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'image_codes/(?P<uuid>.+)/', views.ImageCodeView.as_view()),
    re_path(r'sms_codes/(?P<mobile>\d+)/',views.SMSCodeView.as_view()),
]
