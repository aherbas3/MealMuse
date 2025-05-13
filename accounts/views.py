from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(response):
    return HttpResponse("<h1>hello world!</h1>")

def v1(response):
    return HttpResponse("<h1>this is view 1</h1>")