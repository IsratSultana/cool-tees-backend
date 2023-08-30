from django.shortcuts import render
from .models import Product
from .serializers import ProductSerializer
from apps.users.mixins import CustomLoginRequiredMixin
from rest_framework import generics
# Create your views here.

class ProductList(CustomLoginRequiredMixin,generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=ProductSerializer
    #filter_backends=[DjangoFilterBackend]
    #filterset_fields = ['user_id']
    def get(self,request,*args,**kwargs):
        self.queryset=Product.objects.order_by('created_at').filter(user=request.login_user)
        return self.list(request,*args,**kwargs)