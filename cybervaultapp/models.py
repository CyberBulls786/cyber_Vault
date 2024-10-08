from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    platform = models.CharField(max_length=100)
    username_vault = models.CharField(max_length=100)
    pass_vault = models.CharField(max_length=30, default= '0')
   