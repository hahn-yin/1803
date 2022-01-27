from  django.http import  HttpResponse
from  django.shortcuts import render


def hello(request):
    return HttpResponse("hello world!")


def rehello(request):
    context ={}
    context['hello']='hello world!'
    return  render(request,'test.html',context)