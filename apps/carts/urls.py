from . import views
from django.urls import path

urlpatterns =[
    path('',views.CartList.as_view(),name='cart_list'),
    path('add/',views.CartAdd.as_view(),name='cart_add'),
    path('delete/',views.CartDelete.as_view(),name='cart_delete'),
    path('update/',views.CartUpdate.as_view(),name='cart_update')
]