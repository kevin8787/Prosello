from django.db import models
# from typing_extensions import Required
from django.conf import settings
#from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# User = settings.AUTH_USER_MODEL
# Create your models here.
class Property(models.Model):
    # user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    property_name = models.CharField(max_length=100)
    property_desc = models.CharField(max_length=200)
    property_city = models.CharField(max_length = 50)
    property_address = models.CharField(max_length = 200)
    property_price = models.DecimalField(decimal_places=2, max_digits=20)
    property_owner = models.CharField(max_length=60)
    property_contact = models.CharField(max_length= 10)
    # property_image = models.ImageField(null=True, blank=True, upload_to='images/')

