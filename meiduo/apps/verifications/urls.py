from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r'image_codes/(?P<uuid>.+)/', views.ImageCodeView.as_view())
]
