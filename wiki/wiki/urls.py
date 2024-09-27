"""
1. Add an import:  from my_app import views
2. Add a URL to urlpatterns:  path('', views.home, name='home')
"""
from django.contrib import admin
from django.urls import path

from django.conf import settings
from django.conf.urls.static import static

from core.views import index,feed,faq,writeups

urlpatterns = [
    path('',index,name='index'),
    path('feed',feed,name='feed'),
    path('writeups',writeups,name='writeups'),
    path('faq',faq,name='faq'),
]
if settings.DEBUG == True:
    urlpatterns.extend([
        path('admin/', admin.site.urls),
    ])
