#encoding=utf-8
"""githuboauth URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from oauth2github import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    #   此处的(?P<id>)中的id必须和views中函数的参数名一致
    url(r'^index/(?P<username>.*?)/(?P<email>.*?)/$', views.index, name='site_index'),
    url(r'^red/', views.red, name='site_red'),
    url(r'^login/', views.login, name='site_login'),
    url(r'^search/', views.search, name='site_search'),
    url(r'^coauth/', views.coauth, name='site_coauth'),
    url(r'^domainapi/', views.domainapi),
    url(r'^coauapi/', views.coauapi),
]
