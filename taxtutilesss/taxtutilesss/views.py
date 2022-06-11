#this file is created by me = Gaurav Rajput



# def index(request):
#
#     return HttpResponse(" <h1> Hello Gaurav kse ho yar  how to prepare your python </h1>")
#
# def aboutus(request):
#     return HttpResponse("it is our web page . you surfing any time here ")

from django.http import HttpResponse


def url(request):
    return HttpResponse('''<h1>         My all five links that i use mostly     </h1><a  
    href="https://www.youtube.com/playlist?list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9"> <h1>Dhango play list link</h1></a><a  
    href="https://www.youtube.com/playlist?list=PLu0W_9lII9ahfRrhFcoB-4lpp9YaBmdCP"> <h1> Python oops playlist link</h1></a><a  
    href="https://www.youtube.com/playlist?list=PL0b6OzIxLPbzf12lu5etX_vjN-eUxgxnr"> <h1> my sql  playlist link</h1></a><a  
    href="https://www.youtube.com/playlist?list=PLu0W_9lII9agICnT8t4iYVSZ3eykIAOME"> <h1> my fav PYTHON playlist link</h1></a><a  
    href="https://www.youtube.com/playlist?list=PLlasXeu85E9cQ32gLCvAvr9vNaUccPVNP"> <h1> My javascript playlist link</h1></a>''')

