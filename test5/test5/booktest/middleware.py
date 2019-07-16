from django.http import HttpResponse

exclude_ips = ['127.0.0.1']


class BlockIPsMiddleware(object):
    """中间件类"""

    def process_view(self, request, view_func, *view_argc, **view_kwargs):
        # 获取用户ip
        user_ip = request.META['REMOTE_ADDR']
        if user_ip in exclude_ips:
            return HttpResponse('<h1>Forbidden</h1>')


class TestMiddleware(object):
    def __init__(self):
        """服务器重启后，响应第一个请求时调用"""
        print('---init-----')

    def process_request(self, request):
        """request对象产生之后，url匹配之前调用"""
        print("----process_request-----")
        # return HttpResponse("process_request")

    def process_view(self, request, view_func, *view_argc, **view_kwargc):
        """url匹配之后，视图函数调用之前"""
        print("----process_view----")
        # return HttpResponse("process_view")

    def process_response(self, request, response):
        """视图函数调用之后, 内容返回给浏览器之前调用"""
        print("----process_response----")
        return response
