from django.shortcuts import render
from django.shortcuts import HttpResponse


def home(request):
    # return HttpResponse('this is home')
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')
