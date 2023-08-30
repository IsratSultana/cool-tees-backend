from django.db import models
from apps.users.models import User
from apps.products.models import Product
# Create your models here.

class Cart(models.Model):
  
  user_id=models.ForeignKey(
   User,null=False,blank=False,on_delete=models.CASCADE
  )

  product_id=models.ForeignKey(
    Product,null=False,blank=False,on_delete=models.CASCADE
  )

  quantity=models.IntegerField(
   'quantity',null=False,blank=False
  )

  created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
  )

  updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
  )