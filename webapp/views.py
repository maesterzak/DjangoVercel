from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    message = "Example Django project on vercel"
    return HttpResponse(message)