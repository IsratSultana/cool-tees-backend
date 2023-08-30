from django.db import models
from cloudinary.models import CloudinaryField

gender = (("Men", "Men"), ("Women", "Women"))
# Create your models here.
class Product(models.Model):
    type=models.CharField(
        "type",max_length=50,null=False,blank=False, default="none", choices=gender
    )
    name = models.CharField(
        "name", max_length=50, null=False, blank=False
    )
    description=models.CharField(
        "description", max_length=255,null=False,blank=False
    )
    price= models.FloatField(
        null=False,blank=False
    )
    image=CloudinaryField(
        null=False,blank=False
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
    