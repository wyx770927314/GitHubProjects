from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import FormView, CreateView, UpdateView, DeleteView, MonthArchiveView

from fourthapp.form import CarForm
from fourthapp.models import Car


def result(request):
    return HttpResponse('Success!!!!!!!!!!')


class index(FormView):
    initial = {'name': 'Betty', 'age': '22'}
    template_name = 'fourth.html'
    # success_url为视图类index提供路由地址
    success_url = 'result'
    # form_class所设置的表单在实例化之后可再模板里使用上下文form.as_p生成表格
    form_class = CarForm
    extra_context = {'title': '人员信息表!!!'}


class create_view(CreateView):
    # 初始数据
    initial = {'name': 'create', 'age': '90'}
    template_name = 'fourth.html'
    success_url = 'result'
    # 表达生成方式一
    # form_class = CarForm
    # 表单生成方式二
    model = Car
    # fields设置模型字段，从而生成表单字段
    fields = {'name', 'age'}
    extra_context = {'title': '人员信息表!!!'}


class update_view(UpdateView):
    template_name = 'fourth.html'
    success_url = 'result'
    model = Car
    fields = {'age', 'name'}
    # 路径传过来的age参数
    slug_url_kwarg = 'age'
    # 按照age列来查询
    slug_field = 'age'
    context_object_name = 'car'
    extra_context = {'title': '汽车表'}


class delete_view(DeleteView):
    template_name = 'fourth_delete.html'
    success_url = 'result'
    slug_url_kwarg = 'name'
    slug_field = 'name'
    model = Car
    context_object_name = 'car'
    extra_context = {'title': '汽车表'}


class monthview(MonthArchiveView):
    extra_context = {'title': '汽车信息表'}
    allow_empty = True
    # 是否允许设置是未来的日期
    allow_future = True
    context_object_name = 'carlist'
    template_name = 'fourth_month.html'
    model = Car
    # 通过该字段对数据表进行查询
    date_field = 'date'
    queryset = Car.objects.all()
    # 设置年份的数据格式
    year_format = '%Y'
    # 设置月份的数据格式
    month_format = '%m'
    paginate_by = 50
