from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango say hey there partner!<a href='/rango/about/'>About</a>")


def about(request):
    return HttpResponse("Rango says here is the page.<a href='/rango/'>Index</a>")
