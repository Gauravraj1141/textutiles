#this file is created by me = Gaurav Rajput




# def index(request):
#
#     return HttpResponse(" <h1> Hello Gaurav kse ho yar  how to prepare your python </h1>")
#
# def aboutus(request):
#     return HttpResponse("it is our web page . you surfing any time here ")

from django.http import HttpResponse
from django.shortcuts import render # ye templates k liye import kiya h


def index(request):
    return render(request, 'index.html')


    # return HttpResponse("<h1>Home</h1>")

def removepunc(request):
    return render(request, 'removepunc.html')
    # return HttpResponse("<h1>remove punc</h1>")

def capitalizefirst(request):
    return HttpResponse("<a href = '/' back> </a>")

def newlineremove(request):
    return HttpResponse("<h1>newlineremove</h1>")

def spaceremover(request):
    return HttpResponse("<h1>spaceremover</h1>")
def charcount(request):
    return HttpResponse("<h1>charcount</h1>")
