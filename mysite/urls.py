"""mysite URL Configuration

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
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

admin.autodiscover()

from restaurants.views import menu, list_restaurants, comment
from mysite.views import welcome, use_session, session_test, set_c, get_c, index, register
from django.contrib.auth.views import login, logout

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^welcome/$', welcome),
    url(r'^menu/$', menu),
    url(r'^menu/(\d{1,5})/$', menu),
    url(r'^restaurants_list/$', list_restaurants),
    url(r'^comment/(\d{1,5})/$', comment),
    url(r'^use_session/$', use_session),
    url(r'^session_test/$', session_test),
    url(r'^get_c/$', get_c),
    url(r'^set_c/$', set_c),
    #url(r'^accounts/login/$',login),
    url(r'^accounts/login/$',login,{'template_name':'login.html'}),
    url(r'^accounts/logout/$',logout),
    url(r'^$',index),
    url(r'index/^$',index),
    url(r'^accounts/register/$',register),
]


