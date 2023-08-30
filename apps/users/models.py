from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(
        "name", max_length=50, null=False, blank=False
    )
    password = models.CharField(
        "password", max_length=255,null=False, blank=False 
    )
    email = models.EmailField(
        "email", max_length=255,null=False, blank=False
    ) 
    token = models.CharField(
    "token", max_length=500 ,null=False, blank=False
    )

    token_expires_at=models.DateTimeField(
    'token_expires_at', null=False, blank=False
    )
    created_at = models.DateTimeField(
        'Created Datetime', blank=True, auto_now_add=True
    )
    updated_at = models.DateTimeField(
        'Updated Datetime', blank=True, auto_now=True
    )