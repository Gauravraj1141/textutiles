from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index2.html')


def analyze(request):
    djtext = request.POST.get('text','default')
    removepunc = request.GET.get('removepunc','off')
    uppercase = request.GET.get('uppercase','off')
    newlineremove = request.GET.get('newlineremove','off')
    spaceremover = request.GET.get('spaceremover','off')
    charcount = request.GET.get('charcount','off')


    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed =  analyzed + char
        params = {'purpose': 'Removed Punctutaions', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)
    elif uppercase  == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char
            analyzed = analyzed.upper()
        params = {'purpose': 'Upper case', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    elif newlineremove == "on":
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char
        params = {'purpose': 'Newlineremove', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    elif spaceremover == "on":
        analyzed = ""
        for i , char  in enumerate(djtext):
            if not(djtext[i]== " " and djtext[i+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'space Remove', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)

    elif charcount == "on":

        analyzed = 0
        for char in djtext:
            analyzed = analyzed + len(char)



        params = {'purpose': 'Character Count', 'analyzed_text': analyzed}
        return render(request, 'analyze2.html', params)



    else:
        return HttpResponse("error")




