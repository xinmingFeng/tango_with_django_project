from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    context_dict = {'boldmessage':'Crunchy,creamy,cookie,candy,cupcake!'}
    return render(request,'rango/index.html',context=context_dict)
    return HttpResponse("Rango says hey there partner!<a href='/rango/about/'>About</a>")


def about(request):
    context_dict = {'boldmessage': 'This tutorial has been put together by xinming Feng.'}
    return render(request,'rango/about.html',context=context_dict)
    return HttpResponse("Rango says here is the page.<a href='/rango/'>Index</a>")
    