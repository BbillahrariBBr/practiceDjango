from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(response):
    return HttpResponse('This is second app Contact View')

def about(response):
    return HttpResponse('This is second app About View')