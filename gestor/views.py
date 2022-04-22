from django.http.response import HttpResponse
from django.shortcuts import render


# Create your views here.


def home(request):
    return render(request,'index.html')

def clients(request):
    return render(request,'clients.html')

def login(request):
    return render(request,'login.html')