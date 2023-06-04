from typing import Any
from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=120)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length = 80)
    is_admin = models.BooleanField(default=False)
    image_file = models.CharField(max_length=300)
    is_authenticated= models.BooleanField(default=False)

