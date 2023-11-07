from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class CustomUser(AbstractUser):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=30)
    pass