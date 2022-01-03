from django.contrib import admin
from django.urls import path
from chasma import views
urlpatterns = [
    path('',views.index),
    path('detail/<int:id>/',views.detail),
    path('contact/',views.contact),
    path('search/',views.searchProduct),
    path('addtocart/',views.addtocart),
    path('cart/',views.cart),
    path('plus-cart/',views.updateCart),
    path('minus-cart/',  views.decreaseCart),
    path('delete-cart/',  views.reomveCart),
    path('payment/',  views.payment),
    path('sunglass/',  views.sunglass),
    path('order/',  views.order),
    path('payment/',  views.payment),
]
