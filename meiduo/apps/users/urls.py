from django.urls import path, re_path

from . import views

urlpatterns = [
    re_path(r'^register/', views.Register.as_view()),
    re_path(r'^usernames/(?P<username>\w{5,20})/count/$', views.CheckUsernameView.as_view()),
    re_path(r'^mobiles/(?P<mobile>\d+)/count/$', views.CheckMobileView.as_view()),
    re_path(r'^login/$', views.LoginView.as_view()),
    re_path(r'^info/$', views.UserInfoView.as_view()),
    re_path(r'^emails/$', views.EmailView.as_view()),
    re_path(r'^addresses/$', views.AddressesView.as_view()),
    re_path(r'^addresses/create/$', views.AddressesCreateView.as_view()),
    re_path(r'^addresses/(?P<address_id>\d+)/$', views.AddressesUpdateView.as_view()),
    re_path(r'^addresses/(?P<address_id>\d+)/default/$', views.AddressesDefaultView.as_view()),
    re_path(r'^addresses/(?P<address_id>\d+)/title/$',views.AddressesTitleView.as_view()),
]
