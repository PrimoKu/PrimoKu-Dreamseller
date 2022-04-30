from django.http import HttpResponse
from django.shortcuts import render

def homepage(req):
    # return HttpResponse('Home')
    return render(req, 'home/index.html')

def aboutmePage(req):
    return render(req, 'home/aboutme.html')