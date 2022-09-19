from email.policy import default
from django.db import models
from django.contrib.auth.models import AbstractUser

#class CustomUser(AbstractUser):
#    is_caregiver = models.BooleanField(default=False)
#    is_client = models.BooleanField(default=False)
    

class Service(models.Model):
    name = models.TextField(null=True)
    desc = models.TextField(null=True)
