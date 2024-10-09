from django.db import models
from django.utils import timezone
from accounts.models import User

# Create your models here.
class Lost(models.Model):
    image = models.ImageField(upload_to='%Y%m%d/', blank=True, null=True)
    lostdate = models.TextField(blank=True, null=True)
    losttime = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    
    moredesc = models.TextField(blank=True, null=True)
    founded = models.BooleanField(default=False)
    
    getwhere = models.TextField(blank=True, null=True)
    nowwhere = models.TextField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)

    userget = models.ForeignKey(User, on_delete=models.CASCADE, related_name='itemuserget')

    def __str__(self):
        return str(self.id)