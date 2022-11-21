from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def first(request):
      return HttpResponse('this is our first view function')

def propose(request):
      return HttpResponse('')

def rejection(request):
      return HttpResponse('<h1></h1>')
