from django.db import models
from django.conf import settings

# User = settings.AUTH_USER_MODEL
# Create your models here.
class Property(models.Model):
    # User = models.ForeignKey(User, on_delete=models.CASCADE)
    property_name = models.CharField(max_length=100) 
    property_desc = models.CharField(max_length=200) 
    property_city = models.CharField(max_length = 50)
    property_address = models.CharField(max_length = 200)
    property_price = models.DecimalField(decimal_places=2, max_digits=20)
    property_owner = models.CharField(max_length=60)
    property_contact = models.CharField(max_length= 10)
    