from django.db import models
from django.utils import timezone

# Create your models here.
class Notice(models.Model):
    title = models.TextField(unique=True)
    noticeDate = models.DateTimeField(default=timezone.now)
    contents = models.TextField(unique=True)

    def __str__(self):
        return self.title
    
class PointShop(models.Model):
    stuff = models.TextField(unique=True, blank=True, null=True)
    shop = models.TextField(blank=True, null=True)
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