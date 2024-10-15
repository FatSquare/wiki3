from django.shortcuts import render
from .models import Feed,Writeup
from django.http import Http404

# Create your views here.
def index(request):
    return render(request, 'index.html')

def feed(request):
    feeds = Feed.objects.all()
    return render(request,'feed.html',{
        'feeds' : feeds, 
    })

def writeups(request):
    writeups = Writeup.objects.all()
    return render(request,'writeups.html',{
        'writeups': writeups,    
    })

def faq(request):
    return render(request,'faq.html')

def potato(request):
    return render(request,'potato.html')

def writeup(request,title):
    try:
        writeup = Writeup.objects.get(title=title)
        return render(request,f'writeups/{writeup.page_path}')
    except:
        raise Http404 

    
def test(request):
    return render(request,'test.html')
