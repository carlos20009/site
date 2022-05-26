from django.http import HttpResponse
from django.shortcuts import render
from .models import Client
from .models import Pay

def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")