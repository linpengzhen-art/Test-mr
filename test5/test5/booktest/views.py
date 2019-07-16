from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.core.paginator import Paginator  # 导入分页类

# Create your views here.
# /static_test/
from booktest.models import AreaInfo


def static_test(request):
    """静态文件"""
    return render(request, "booktest/static_test.html")


# exclude_ips = ['127.0.0.1']

# /index/
"""
def index(request):
    # 获取用户的ip地址
    user_ip = request.META['REMOTE_ADDR']
    # print(user_ip)
    if user_ip in exclude_ips:
        return HttpResponse('<h1>Forbidden</h1>')
    return render(request, "booktest/index.html")
"""


def index(request):
    print('---index-----')
    return render(request, "booktest/index.html")


def area(request, pindex):
    """分页"""
    # 1.获取所有省级地区信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    # 2. 进行分页
    paginator = Paginator(areas, 10)
    # print(paginator.num_pages)  # 分页后的总页数
    # print(paginator.page_range)  # 页码的列表
    # print(paginator.count)  # 分页数据的总数目

    # 默认显示第1页
    if not pindex:
        pindex = 1

    # 3. 获取第pindex页的内容
    # <class 'django.co re.paginator.Page'>
    areas = paginator.page(int(pindex))
    # <class 'django.core.paginator.Page'>
    # print(type(areas))
    # <class 'django.db.models.query.QuerySet'>
    # print(type(areas.object_list))
    # print(areas.number)  # 返回当前页的页码
    # print(type(areas.paginator)) # 当前分页Paginator类对象

    # areas.has_previous()  # 当前页是否有上一页
    # areas.has_next()  # 当前页是否有下一页
    # areas.next_page_number()  # 当前页下一页页码
    # 4. 使用模板文件
    return render(request, "booktest/area.html", {"areas": areas})


# /show_area/
def show_area(request):
    """显示省市县选择页面"""
    return render(request, "booktest/show_area.html")


def get_prov(request):
    """获取省级地区信息"""
    # 1. 查询出省级地区信息
    areas = AreaInfo.objects.filter(aParent__isnull=True)
    area_list = []
    # 2. 拼接出json数据
    for area in areas:
        area_list.append((area.id, area.atitle))
    # 3. 返回json数据
    return JsonResponse({'data': area_list})


# /city/
def get_city(request, pid):
    """获取市的信息"""
    # 根据pid，其下子集信息
    # area = AreaInfo.objects.get(id=pid)
    # areas = area.areainfo_set.all()
    areas = AreaInfo.objects.filter(aParent__id=pid)
    area_list = []
    # 2. 拼接出json数据
    for area in areas:
        area_list.append((area.id, area.atitle))
    # 3. 返回json数据
    return JsonResponse({'data': area_list})

# def get_dis()
