from django.shortcuts import render
from .models import Feed,Writeup
from django.http import Http404,HttpResponse

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

def writeup(request,wid):
    try:
        writeup = Writeup.objects.get(wid=wid)
        return render(request,f'writeups/{writeup.page_path}')
    except:
        raise Http404 

    
def test(request):
    return render(request,'test.html')

def robots(_request):
    content = (
        "User-agent: *\n"
        "Allow: /\n"
        "Allow: /writeup/Securinets_Quals_2024\n"
    )
    return HttpResponse(content, content_type="text/plain")
