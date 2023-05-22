from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def info(response):
    return HttpResponse('This is first app info View')

def house(response):
    return HttpResponse('This is first app House View')