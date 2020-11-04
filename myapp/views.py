from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello everyone how are you peopple,<h1>this is HARIOM</h1>')
