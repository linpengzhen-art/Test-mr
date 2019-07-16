from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^index/$', views.index),  # 首页
    url(r'^login/$', views.login),  # 显示登录页面
    url(r'^login_check/$', views.login_check),  # 登录校验
    url(r'^login_ajax/$', views.login_ajax),  # ajax登录页面
    url(r'^login_ajax_check/', views.longin_ajax_check),  # ajax登录校验
    url(r'^show_add/$', views.show_add),  # 显示自增页面
    url(r'^get_add/$', views.get_add)  # 实现自增
]
