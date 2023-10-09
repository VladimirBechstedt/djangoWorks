from django.urls import path
from . import views

urlpatterns = [
    path('main/', views.main, name='main'),
    path('about_me/', views.about_me, name='about_me'),
    path('orders/<int:pk>/<int:day>/', views.orders, name='orders'),
    path('order/<int:order_pk>/', views.order, name='order'),
]
