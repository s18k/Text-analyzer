# i have created this file
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    #params={'name':'Shreyas Kamath','place':'Pune'}
    return render(request,'index.html')
    #return HttpResponse("Hello")
# def about(request):
#     return HttpResponse("About")

def analyze(request):
    # get the text
    djtext = request.GET.get('text','default')
    # check which is ticked

    fullcaps=request.GET.get('fullcaps','off')
    removespace=request.GET.get('removespace','off')
    charcount=request.GET.get('charcount','off')
    wordcount=request.GET.get('wordcount','off')
    no_word=0
    no_char=0
    todo=""
    params={}
    print(fullcaps)
    print(removespace)
    finalstring=""
    #if punctuation
    if(fullcaps=="on"):
        todo+="\nChanged to Upper Case"
        analyzed=""
        for char in djtext:
            analyzed+=char.upper()
        djtext=analyzed

    print(djtext)

    if(removespace=="on"):
        analyzed=""
        for i in range(0,len(djtext)):
            if(djtext[i]==" "):
                if(djtext[i+1]!=" "):
                    analyzed+=djtext[i]
            else:
                analyzed+=djtext[i]
        djtext=analyzed
        finalstring=analyzed

    print(djtext)
    if(charcount=="on"):
        c=0
        for i in djtext:
            if(i!=" "):
                c+=1
        no_char=c

    if(wordcount=="on"):
        for i in range(0,len(djtext)-1):
            if(djtext[i]==" " and djtext[i+1]!=" "):
                analyzed+=djtext[i]
        djtext=analyzed
        no_word=djtext.count(" ")+1

    print(djtext)
    if(charcount=="on" and wordcount=="on"):
        params = {'newtext': analyzed,'charcount':no_char,'wordcount':no_word}
    elif(charcount=="on"):
        params = {'newtext': analyzed, 'charcount': no_char, 'wordcount': "NA"}
    else:
        params = {'newtext': analyzed, 'charcount': "NA", 'wordcount': no_word}
    return render(request,'analyze.html',params)
# def capfirst(request):
#     return HttpResponse("Capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("New Line remove")
#
#
# def spaceremove(request):
#     return HttpResponse("space remove")
#
# def charcount(request):
#     return HttpResponse("char count")