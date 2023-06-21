from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    message = "Example Django project on vercel"
    return HttpResponse(message)


def database_view(request):
    post = Post.objects.get(id = 1)
    message = post.body
    return HttpResponse(message)
