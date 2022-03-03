from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
import os

# Create your views here.
from django.urls import reverse


def uploadfile(request):
    if request.method == 'POST':
        myFile = request.FILES.get('myfile')
        if not myFile:
            return HttpResponse('无文件')
        # 找到文件的存放目录，开始写入提交上来的文件
        f = open(os.path.join('/Users/fanler/Downloads', myFile.name), 'wb+')
        for chunk in myFile.chunks():
            f.write(chunk)
        f.close()
        return HttpResponse('上传完成')
    else:
        return HttpResponse('发送的请求为get请求')


def make_cookies(request):
    # cookie是以字典的形式存储的
    uuid = request.COOKIES.get('uuid')
    print(uuid)
    # uuid = request.COOKIES['uuid']
    if uuid:
        try:
            request.get_signed_cookie('uuid',salt='DjangoProject')
        except:
            raise Http404('当前Cookie无效哦！')
        return HttpResponse('当前cookie为:'+uuid)
    else:
        raise Http404('当前访问没有Cookie哦！')


def create(request):
    response = redirect(reverse('secondapp:index'))
    response.set_cookie('uid','Cookie_Value')
    response.set_signed_cookie('uuid','ididid',salt='DjangoProject',max_age=10)
    return response


def index(request):
    return render(request, 'index.html')
