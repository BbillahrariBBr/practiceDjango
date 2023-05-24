from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contact(response):
    return HttpResponse('''
                        <h1>This is second app Contact View</h1>
                        <a href= '/second_app/about'>About</a>
                        <a href= '/first_app/info'>Info</a>
                        <a href= '/first_app/house'>House</a>
                        ''')

def about(response):
    return HttpResponse('''
                        <h1>This is second app About View</h1>
                        <a href= '/second_app/contact'>contact</a>
                        <a href= '/first_app/info'>Info</a>
                        <a href= '/first_app/house'>House</a>
                        ''')