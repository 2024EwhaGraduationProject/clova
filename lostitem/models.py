from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.
class Lost(models.Model):
    image = models.ImageField(upload_to='%Y%m%d/', blank=True, null=True)
    lostdate = models.CharField(blank=True, null=True, max_length=255)
    losttime = models.CharField(blank=True, null=True, max_length=255)
    description = models.CharField(blank=True, null=True, max_length=255)
    title = models.CharField(blank=True, null=True, max_length=255)
    
    moredesc = models.CharField(blank=True, null=True, max_length=255)
    founded = models.BooleanField(default=False)
    
    getwhere = models.CharField(blank=True, null=True, max_length=255)
    nowwhere = models.CharField(blank=True, null=True, max_length=255)
    category = models.CharField(blank=True, null=True, max_length=255)

    userget = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itemuserget')

    def __str__(self):
        return str(self.id)