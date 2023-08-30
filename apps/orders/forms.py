from .models import Order,OrderItems
from django import forms


class OrderForm(forms.ModelForm):
    class Meta:
        model= Order
        fields ='__all__'

class OrderItemForm(forms.ModelForm):
    class Meta:
        model= OrderItems
        fields ='__all__'