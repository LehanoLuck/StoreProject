from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser (AbstractUser):
    city = models.CharField(max_length=250)
    street = models.CharField(max_length=250)
    house = models.CharField(max_length=250)
# Create your models here.
