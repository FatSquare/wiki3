from django.shortcuts import render
from .models import Feed

# Create your views here.
def index(request):
    return render(request, 'index.html')

def feed(request):
    feeds = Feed.objects.all()
    return render(request,'feed.html',{
        'feeds' : feeds, 
    })

def writeups(request):
    return render(request,'writeups.html')

def faq(request):
    return render(request,'faq.html')

def potato(request):
    return render(request,'potato.html')
