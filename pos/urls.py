from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list, name = 'product_list'),
    path('create_order', views.create_order, name = 'create_order'),

    path('order/<int:order_id>/', views.order_detail, name = 'order_detail')
]
