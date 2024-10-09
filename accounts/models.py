from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    nickname = models.CharField(max_length=200)
    profile = models.ImageField(upload_to='%Y%m%d/', blank=True, null=True)
    luckypoint = models.IntegerField(default=0, blank=True, null=True)

    def __str__ (self):
        return self.nickname