from django.shortcuts import render
from django.http.response import HttpResponse
from django.http.request import HttpRequest
# Create your views here.

def hello_world(request: HttpRequest):
    return HttpResponse('<h1>Hello world!</h1>')


def my_name(request: HttpRequest):
    return HttpResponse('<h1>Bekzhan</h1>')