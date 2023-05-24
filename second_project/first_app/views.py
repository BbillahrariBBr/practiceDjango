from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def info(response):
    return HttpResponse('''
                        <h1>This is first app info View</h1>
                        <a href= '/first_app/house'>House</a>
                        <a href= '/second_app/about'>About</a>
                        <a href= '/second_app/contact'>contact</a>
                        ''')

def house(response):
    return HttpResponse('''
                        <h1>This is first app House View</h1>
                        <a href= '/first_app/info'>Info</a>
                        <a href= '/second_app/about'>About</a>
                        <a href= '/second_app/contact'>contact</a>
                        ''')