"""
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from django.conf import settings
from django.conf.urls.static import static

from core.views import index,feed,faq,writeups,potato,test,writeup,robots

urlpatterns = [
    path('',index,name='index'),
    path('feed',feed,name='feed'),
    path('writeups',writeups,name='writeups'),
    path('writeup/<int:wid>',writeup),
    path('faq',faq,name='faq'),
    path('p0tato',potato,name='p0tato'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=False)),
    path('robots.txt',robots)
]
if settings.DEBUG == True:
    urlpatterns.extend([
        path('admin/', admin.site.urls),
        path('test/', test),
    ])
