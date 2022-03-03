from django.urls import path

from fourthapp import views
from fourthapp.views import index, result, create_view, update_view, delete_view

urlpatterns = [
    path('', index.as_view(), name='index'),
    path('result', result, name='result'),
    path('create/', create_view.as_view(), name='create'),
    path('create/result', result, name='create_result'),
    path('update/<age>.html', update_view.as_view(), name='update'),
    path('update/result', result, name='update_result'),
    path('delete/<name>.html', delete_view.as_view(), name='delete'),
    path('delete/result', result, name='delete_result'),
    path('<int:year>/<int:month>.html',views.monthview.as_view(),name='month'),
]
