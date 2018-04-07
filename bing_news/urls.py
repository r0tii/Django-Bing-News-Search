"""bing_news URL Configuration
"""
from django.conf.urls import url, include
from django.contrib import admin
from newsapp import views
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home, name='home'),
]


