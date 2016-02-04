"""DjangoCRUD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from crud.views import FooList, Index, FooCreate, FooEdit, BarCreate,BarEdit,BarList,\
    FooDelete, BarDelete

urlpatterns = [
    url(r'^$',Index.as_view(),name='crud.list'),
    #foo
    url(r'^foo/list/$',FooList.as_view(),name='crud.foo.list'),
    url(r'^foo/create/$',FooCreate.as_view(),name='crud.foo.create'),
    url(r'^foo/edit/(?P<id>[^/]+)/$',FooEdit.as_view(),name='crud.foo.edit'),
    url(r'^foo/delete/(?P<id>[^/]+)/$',FooDelete.as_view(),name='crud.foo.edit'),
    #bar
    url(r'^bar/list/$',BarList.as_view(),name='crud.bar.list'),
    url(r'^bar/create/$',BarCreate.as_view(),name='crud.bar.create'),
    url(r'^bar/edit/(?P<id>[^/]+)/$',BarEdit.as_view(),name='crud.bar.edit'),
    url(r'^bar/delete/(?P<id>[^/]+)/$',BarDelete.as_view(),name='crud.bar.edit'),
    
]
