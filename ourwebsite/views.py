from django.http import HttpResponse
from django.shortcuts import render
def index(request):

    return render(request, 'index.html')
    # return HttpResponse("Home")
def about(request):
    return HttpResponse("This is the about page ")
def ex1(request):
    d = '''<h2>NAVIGATION BAR<br></h2>
                <a href="https://youtu.be/h3sxUR6i8tc">ARJIT SINGH SONG</a><br>
                <a href="https://www.freecodecamp.org/"> FREECODECAMP <a/><br>
                <a href="https://www.hdfcbank.com/">HDFC NETBANKING <a/><br>
                
                    <p> Welcome to this attractive website .....</p>
    '''
    return HttpResponse(d)
    #get the text
def analyze(request):
    djtext = request.POST.get('text', 'default')
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')

    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':'Removed punctuation', 'analyzed_text': analyzed}
        djtext = analyzed
    if(fullcaps == "on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed+char.upper()
        params = {'purpose': 'Change to Uppercase', 'analyzed_text': analyzed}
        djtext = analyzed
    if(newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed+char
        params = {'purpose': 'Change to newlineremover', 'analyzed_text': analyzed}
        djtext = analyzed
    if(extraspaceremover == "on"):
        analyzed = ""
        for index , char in enumerate(djtext):
            if not(djtext[index] == " " and djtext[index+1] == " "):
            #     pass
            # else: if we not use the not function then we can use pass and else statement..............

                analyzed = analyzed + char
        params = {'purpose': 'Change to extraspaceremover', 'analyzed_text': analyzed}
    if(removepunc !="on" and fullcaps != "on " and newlineremover != "on" and extraspaceremover != "on"):
        return HttpResponse("Error")



    return render(request, 'analyze.html', params)
