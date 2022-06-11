#this file is created by me = Gaurav Rajput



# def index(request):
#
#     return HttpResponse(" <h1> Hello Gaurav kse ho yar  how to prepare your python </h1>")
#
# def aboutus(request):
#     return HttpResponse("it is our web page . you surfing any time here ")

from django.http import HttpResponse
def file(request):
    f = open("gaurav2.txt", "r+")



    return HttpResponse(f.read(),f.write("<h1>  Gaurav is good developer <\h1>"),)

