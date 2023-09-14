from django.shortcuts import render
from django.http import HttpResponse

def index_views(request):
    return HttpResponse("<h1>home page</h1>")

def contact_views(request):
    return HttpResponse("hi this is contacr page")

def about_views(request):
    return HttpResponse("this is about page")


# Create your views here.
