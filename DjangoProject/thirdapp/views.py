from django.shortcuts import render
from django.views.generic import RedirectView, TemplateView, ListView, DetailView

# Create your views here.
from thirdapp.models import PersonInfo


def index(request):
    return render(request, 'third.html')


class turnToRedirectView(RedirectView):
    url = None
    permanent = False
    pattern_name = 'thirdapp:index'
    query_string = True

    def get_redirect_url(self, *args, **kwargs):
        print('This is get_redirect_url!!')
        # return super(turnTo, self).get_redirect_url(*args, **kwargs)
        return super().get_redirect_url(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        print('This is get!!')
        print(request.META.get('HTTP_USER_AGENT'))
        # return super().get(request, *args, **kwargs)
        return super(turnToRedirectView, self).get(request, *args, **kwargs)


class turnToTemplateView(TemplateView):
    template_name = 'third.html'
    template_engine = None
    content_type = None
    extra_context = {'title': 'This is Title!!!'}

    # 重新定义模板上下文的获取方式
    def get_context_data(self, **kwargs):
        context = super(turnToTemplateView, self).get_context_data(**kwargs)
        # context=super().get_context_data(**kwargs)
        context['value'] = 'I am Django!!!'
        return context

    # 定义HTTP的POST请求处理方法
    # 参数request代表HTTP请求信息，如路设有变量则可从参数kwargs里获取
    def post(self, request, *args, **kwargs):
        self.extra_context = {'title': 'This is POST!!!'}
        context = self.get_context_data(**kwargs)
        return self.render_to_response(context)

class turnToListView(ListView):
    #设置模板文件
    template_name = 'third.html'
    #设置模型外的数据
    extra_context = {'listview_title':'人员信息表'}
    #查询模型PersonInfo的所有数据
    queryset = PersonInfo.objects.all()
    #每页展示一条数据
    paginate_by = 1
    #若不设置，则模板上下文默认为personinfo_list
    context_object_name = 'listview_personinfo'

class turnToDetailView(DetailView):
    # 设置模板文件
    template_name = 'third.html'
    # 设置模型外的数据
    extra_context = {'title':'This is DetailView'}
    #设置模型的查询字段
    slug_field = 'age'
    #设置路由的变量名,与属性slug_field实现模型的查询操作
    slug_url_kwarg = 'age'
    pk_url_kwarg = 'pk'
    #设置查询模型PersonInfo
    model = PersonInfo
    #属性queryset可以做简单的查询操作
    #queryset = PersonInfo.objects.all()
    #如不设置，则模板上下文默认为personinfo
    #context_object_name = 'personinfo'
    #是否将pk和slug作为查询条件
    #query_pk_and_slug = False

def hello(request):
    return render(request, 'hello.html')
