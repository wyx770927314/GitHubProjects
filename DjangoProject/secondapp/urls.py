from django.urls import path

from secondapp import views

urlpatterns = [
    path('index/',views.index,name='index'),
    path('upload/', views.uploadfile, name='uploadfile'),
    path('create/',views.create,name='create'),
    path('cookie/',views.make_cookies,name='make_cookies')
]
