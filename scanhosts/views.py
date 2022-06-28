from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.

def getinfo(request):
    return HttpResponse("index")


def sendinfo(request):
    return HttpResponse("sendinfo")
