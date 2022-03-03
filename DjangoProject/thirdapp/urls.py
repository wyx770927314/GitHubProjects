from django.urls import path
from django.views.generic import ListView

from thirdapp import views
from thirdapp.views import turnToRedirectView, turnToTemplateView, turnToListView, turnToDetailView

urlpatterns = [
    path('index/', views.index, name='index'),
    path('turnToRedirectView/', turnToRedirectView.as_view(), name='turnToRedirectView'),
    path('hello', views.hello, name='hello'),
    path('turnToTemplateView/', turnToTemplateView.as_view(), name='turnToTemplateView'),
    path('turnToListView/', turnToListView.as_view(), name='turnToListView'),
    path('<pk>/<age>.html', turnToDetailView.as_view(), name='turnToDetailView'),
]
