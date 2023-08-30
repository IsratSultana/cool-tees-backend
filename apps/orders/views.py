from django.shortcuts import render
from apps.users.mixins import CustomLoginRequiredMixin
from rest_framework import generics
from rest_framework import status
from .models import Order
from apps.carts.models import Cart
from .serializers import OrderSerializer
from .forms import OrderForm,OrderItemForm
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


# Create your views here.
class OrderAdd(CustomLoginRequiredMixin, generics.CreateAPIView):
    queryset = Order.objects.all()
    serializer=OrderSerializer

    def get(self, request ,*args, **kwargs):
        print(request)
        self.queryset = Cart.objects.order_by('-created_at').filter(user_id=request.login_user.id)
        return self.list(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        request.data['user_id']=request.login_user.id
        order_form =OrderForm(request.data)

        if not order_form.is_valid() :
            response =Response({"error":"Requested data is incorrect"}, status=status.HTTP_404_NOT_FOUND)   
            response.accepted_renderer = JSONRenderer()
            response.accepted_media_type = 'application/json'
            response.renderer_context ={}
            return response
        
        order=order_form.save()

        #to get the cart items to order of the current user

        carts =Cart.objects.filter(user=request.login_user)

        for cart in carts:
            order_item_form =OrderItemForm({"order":order.id,"product":cart.product.id,"quantity":cart.quantity})
            order_item_form.save()

        carts.delete()

        serializer =OrderSerializer([order],many=True)
        return Response(serializer.data[0])