from django.http import HttpResponse, HttpResponsePermanentRedirect, HttpResponseRedirect, Http404, \
    StreamingHttpResponse, FileResponse
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import resolve, reverse


def mydate(request, year, month, day):
    args = ['2021', '11', '11']
    result = resolve(reverse('firstapp:mydate', args=args))
    print('url_name:', result.url_name)
    print('namespace::', result.namespace)
    print('kwargs:', result.kwargs)
    print('view_name:', result.view_name)
    print('app_name:', result.app_name)
    return HttpResponse(str(year) + '/' + str(month) + '/' + str(day))


def firstfunc(request):
    # # args = ['4422', '12', '12']
    # # kwargs = {'year': '2022', 'month': '10', 'day': '14'}
    # # print(reverse('firstapp:mydate', args=args))
    # # print(reverse('firstapp:mydate', kwargs=kwargs))
    # url = reverse('firstapp:mydate', args=args)
    if request.method == 'GET':
        # 类方法的使用
        print(request.is_secure())
        print(request.is_ajax())
        print(request.get_host())
        print(request.get_full_path())
        print(request.get_raw_uri())
        # 属性的使用
        print(request.method)
        print(request.COOKIES)
        print(request.content_type)
        print(request.content_params)
        print(request.scheme)
        # 获取GET请求的请求参数
        print(request.GET.get('user', ''))
    elif request.method == 'POST':
        print(request.POST.get('user', ''))
    return render(request, 'response.html')
    # return HttpResponse(reverse('firstapp:mydate', args=args))
    # return redirect(url)
    # return HttpResponsePermanentRedirect(url)
    # return HttpResponseRedirect(url)


def page_not_found(request, exception):
    return render(request, '404.html', status=500)


def page_error(request):
    return render(request, '500.html', status=500)


def downloadfile_one(request):
    file_path = '/Users/fanler/Desktop/git命令'
    try:
        r = HttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=git命令'
        return r
    except Exception:
        raise Http404('Download error')


def downloadfile_two(request):
    file_path = '/Users/fanler/Desktop/命令.txt'
    try:
        r = StreamingHttpResponse(open(file_path, 'rb'))
        r['content_type'] = 'application/octet-stream'
        r['Content-Disposition'] = 'attachment;filename=命令.txt'
        return r
    except Exception:
        raise Http404('Download error')


def downloadfile_three(request):
    file_path = '/Users/fanler/Desktop/账号.txt'
    try:
        f = open(file_path, 'rb')
        r = FileResponse(f, as_attachment=True, filename='账号.txt')
        return r
    except Exception:
        raise Http404('Download error')
