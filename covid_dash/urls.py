from django.contrib import admin
from django.urls import path
from django.conf.urls import url
from firstUI import views

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.indexPage, name='index'),
    url('selectCountry', views.indiCountryData, name='indiCountryData' )
]
