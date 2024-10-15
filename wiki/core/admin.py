from django.contrib import admin

# Register your models here.
from .models import Feed,Writeup 

admin.site.register(Feed)
admin.site.register(Writeup)
