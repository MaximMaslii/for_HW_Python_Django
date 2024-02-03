from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.base, name='base'),
    path('clients/', views.read_clients, name='read_clients'),
    path('client/create/', views.create_client, name='create_client'),
    path('client/<int:client_id>/', views.update_client, name='update_client'),
    path('client/<int:client_id>/delete/', views.delete_client, name='delete_client'),

    # Product URLs
    path('products/', views.read_products, name='read_products'),
    path('product/create/', views.create_product, name='create_product'),
    path('product/<int:product_id>/', views.update_product, name='update_product'),
    path('product/<int:product_id>/delete/', views.delete_product, name='delete_product'),

    # Order URLs
    path('orders/', views.read_orders, name='read_orders'),
    path('order/create/<int:client_id>/', views.create_order, name='create_order'),
    path('order/<int:order_id>/', views.update_order, name='update_order'),
    path('order/<int:order_id>/delete/', views.delete_order, name='delete_order'),
]
