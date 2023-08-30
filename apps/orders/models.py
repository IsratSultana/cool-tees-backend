from django.db import models
from apps.products.models import Product
from apps.users.models import User
# Create your models here.
class Order(models.Model):

  class Meta(object):
    db_table='Order'

  user_id=models.ForeignKey(
    User, null=False,blank=False,on_delete=models.CASCADE
  )
  total_price=models.FloatField(
    'total_price',null=False,blank=False
  )
  customer_name=models.CharField(
    'customer_name',max_length=255,null=False,blank=False
  ) 
  address=models.CharField(
    'address',max_length=255,null=False,blank=False
  )
  building_type=models.CharField(
    'building_type',max_length=255,null=True,blank=True
  )
  city=models.CharField(
    'city',max_length=255,null=False,blank=False
  )
  state=models.CharField(
    'state',max_length=255,null=False,blank=False
  )
  pin_code=models.CharField(
    'pin_code',max_length=255,null=False,blank=False
  )
  total_qty=models.IntegerField(
    'total_qty',null=False,blank=False
  )
  customer_phone=models.CharField(
    'customer_phone',max_length=255,null=False,blank=False
  )
  created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
  updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )
   
class OrderItems(models.Model):
    
  class Meta(object):
    db_table='OrderItems'
  order = models.ForeignKey(
    Order, on_delete=models.CASCADE, db_index=True
  )
  product = models.ForeignKey(
    Product, on_delete=models.CASCADE, db_index=True
  )
  quantity =models.IntegerField(
    'Quantity',blank=False, null=False, db_index=True
  )
  created_at = models.DateTimeField(
    'Created Datetime', blank=True, auto_now_add=True
    )
  updated_at = models.DateTimeField(
   'Updated Datetime', blank=True, auto_now=True
    )