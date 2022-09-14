from django.shortcuts import get_object_or_404, render

# Create your views here.
from django.http import HttpResponse
from .models import quotes, links
from datetime import date


def index(request):
    return HttpResponse("Hello, world.")
