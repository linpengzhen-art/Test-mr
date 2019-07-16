from django.conf.urls import url
from booktest import views

urlpatterns = [
    url(r'^static_test/$', views.static_test),  # 静态文件
    url(r'^index/$', views.index),
    url(r'^area/(\d*)/*$', views.area),  # 分页
    url(r'^show_area/$', views.show_area),  # 显示省市县选择页面
    url(r'^prov/$', views.get_prov),  # 获取省级地区信息
    url(r'^city/(\d+)/$', views.get_city),  # 获取市级地区信息
    # url(r'^dis/(\d+)/$', views.get_dis),  # 获取县级地区信息
]
