from django.urls import path
from .views import product_detail_view, product_list_view

urlpatterns = [
    path('', product_list_view, name='product_list'),
    path('product/<slug:product_slug>/', product_detail_view, name='product_detail'),
]
