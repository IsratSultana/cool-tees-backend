from . import views
from django.urls import path

urlpatterns =[
    path('',views.OrderAdd.as_view(),name='order_list')
]