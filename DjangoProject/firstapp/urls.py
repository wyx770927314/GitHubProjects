from django.urls import path
from django.views.generic import RedirectView

from firstapp import views

urlpatterns = [
    path('<year>/<int:month>/<slug:day>', views.mydate, name='mydate'),
    path('', views.firstfunc, name='firstfunc'),
    path('turnTo',RedirectView.as_view(url='/'),name='turnTo'),
    path('downloadfile1/',views.downloadfile_one,name='downloadfile_one'),
    path('downloadfile2/',views.downloadfile_two,name='downloadfile_two'),
    path('downloadfile3/',views.downloadfile_three,name='downloadfile_three'),
]
