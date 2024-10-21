from django.db import models
from django.utils import timezone
# Create your models here.

class Feed(models.Model):
    author = models.CharField(max_length=16,default='squar3')
    title = models.CharField(max_length=64,default='')
    content = models.TextField(default='')
    creation_time = models.DateTimeField(default=timezone.now);
    
    class Meta:
        ordering = ('-creation_time',)
    def __str__(self):
        return self.title

class Writeup(models.Model):
    wid = models.AutoField(default=1,primary_key=True)
    title = models.CharField(max_length=64,default='')
    page_path = models.CharField(max_length=128,default='')
    creation_time = models.DateTimeField(default=timezone.now);
    
    class Meta:
        ordering = ('-creation_time',)
    def __str__(self):
        return self.title
