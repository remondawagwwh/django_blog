from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home (request):
    return HttpResponse("Home page")

def users (request):
    return HttpResponse("user page")

def about (request):
    return HttpResponse("about page")