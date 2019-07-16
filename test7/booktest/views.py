from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect


# Create your views here.

def index(request):
    # a = 'a' + 3
    return render(request, "booktest/index.html")


def delete(requst, bid2):
    return HttpResponse(bid2)


def login(request):
    """显示登录页面"""
    return render(request, 'booktest/login.html')


def login_check(request):
    """登录校验"""
    # request 是一个HttpResponse类型对象，request.POST
    # print(type(request.POST))
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username + ":" + password)
    if 'jun' == username and '123' == password:
        # 登录成功，跳转到首页
        return redirect('/index/')
    else:
        # 登录失败, 跳转到login
        return redirect('/login/')


def login_ajax(request):
    """显示ajax登录页面"""
    return render(request, "booktest/login_ajax.html")


def longin_ajax_check(request):
    """ajax登录校验"""
    # 1. 接收用户输入的用户名和密码
    username = request.GET.get('username')
    password = request.GET.get('password')
    # 2. 登录校验
    if 'jun' == username and '123' == password:
        return JsonResponse({'res': 1})
    # 返回json数据 登录成功 返回{'res': 1} 登录失败返回{'res':0}
    else:
        return JsonResponse({'res': 0})


# /show_add/
def show_add(request):
    """显示自增页面"""
    return render(request, "booktest/show_add.html", )


def get_add(request):
    """自增"""
    # 获取res的值
    res = request.GET.get('res')
    # 自增
    res = int(res) + 1
    return JsonResponse({"res": res})
