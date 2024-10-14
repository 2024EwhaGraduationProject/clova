from django.db import models
from django.utils import timezone

# Create your models here.
class Notice(models.Model):
    title = models.CharField(blank=True, null=True, max_length=255)
    noticeDate = models.DateTimeField(default=timezone.now)
    contents = models.CharField(blank=True, null=True, max_length=255)

    def __str__(self):
        return self.title
    
class PointShop(models.Model):
    stuff = models.CharField(unique=True, blank=True, null=True, max_length=255)
    shop = models.CharField(blank=True, null=True, max_length=255)
    price = models.IntegerField(blank=True, null=True)
    soldout = models.BooleanField(default=False)

    def __str__(self):
        return self.stuff

'''
class Category(models.Model):
    category = models.TextField(unique=True)
    
    def __str__(self):
        return self.category
'''