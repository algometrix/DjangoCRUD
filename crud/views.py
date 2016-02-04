from django.shortcuts import render
from django.views.generic.base import View
from django.http.response import HttpResponseRedirect
from django.views.generic.list import ListView
from crud.models import Foo, Bar
from crud.forms import FooForm, BarForm
from django.core.urlresolvers import reverse
from django.core import serializers

# Create your views here.
class FooList(View):
    def get(self, request):
        params = dict()
        params['objects'] = Foo.objects.all()
        return render(request, 'foo/list.html', params)
    
    def post(self, request):
        return HttpResponseRedirect('/')
    
class FooCreate(View):
    def get(self, request):
        params = dict()
        params['form'] = FooForm()
        return render(request, 'foo/create.html', params)
    
    def post(self, request):
        form = FooForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bar_name = form.cleaned_data['bar_name']
            new_foo = Foo.objects.create(name=name)
            if bar_name != None and bar_name !='':
                Bar.objects.create(foo=new_foo, name=bar_name)
            return HttpResponseRedirect(reverse('crud.foo.list'))
        return HttpResponseRedirect('/')
    
class FooEdit(View):
    def get(self, request, id):
        params = dict()
        object = Foo.objects.get(id=id)
        children = object.bar.all()
        params['form'] = FooForm(initial={'name':object.name})
        params['children'] = children
        return render(request, 'foo/edit.html', params)
    
    def post(self, request,id):
        form = FooForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            bar_name = form.cleaned_data['bar_name']
            object = Foo.objects.get(id=id)
            object.name = name
            object.save()
            if bar_name != None and bar_name !='':
                Bar.objects.create(foo=object, name=bar_name)
            return HttpResponseRedirect(reverse('crud.foo.list'))
        return HttpResponseRedirect('/')
    
class FooDelete(View):
    def get(self, request, id):
        object = Foo.objects.get(id=id)
        object.delete()
        return HttpResponseRedirect(reverse('crud.foo.list'))
    
    def post(self, request):
        return HttpResponseRedirect('/')
    
class BarList(View):
    def get(self, request):
        params = dict()
        params['objects'] = Bar.objects.all()
        return render(request, 'bar/list.html', params)
    
    def post(self, request):
        return HttpResponseRedirect('/')
    
class BarCreate(View):
    def get(self, request):
        params = dict()
        params['form'] = BarForm()
        return render(request, 'bar/create.html', params)
    
    def post(self, request):
        form = BarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            foo_id = form.cleaned_data['foo_id']
            Bar.objects.create(name=name,foo=Foo.objects.get(id=foo_id))
            return HttpResponseRedirect(reverse('crud.bar.list'))
        return HttpResponseRedirect('/')
    
class BarEdit(View):
    def get(self, request, id):
        params = dict()
        object = Bar.objects.get(id=id)
        params['form'] = BarForm(initial={'name':object.name,'foo_id':object.foo.id})
        return render(request, 'bar/edit.html', params)
    
    def post(self, request,id):
        form = BarForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            foo_id = form.cleaned_data['foo_id']
            object = Bar.objects.get(id=id)
            object.name = name
            object.foo = Foo.objects.get(id=foo_id)
            object.save()
            return HttpResponseRedirect(reverse('crud.bar.list'))
        return HttpResponseRedirect('/')
    
class BarDelete(View):
    def get(self, request, id):
        object = Bar.objects.get(id=id)
        object.delete()
        return HttpResponseRedirect(reverse('crud.bar.list'))
    
    def post(self, request):
        return HttpResponseRedirect('/')
    
class Index(ListView):
    def get(self,request):
        return render(request, 'index.html')