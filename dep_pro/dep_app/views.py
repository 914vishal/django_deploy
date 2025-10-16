from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse

# Create your views here.

def welcome(req):
    return HttpResponse("response from deployment");