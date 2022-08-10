from django.urls import path
from .views import *

urlpatterns = [
    path('', StoreView.as_view(), name='store_view'),
    path('products/', ProductView.as_view(), name='product_view'),
    path('filter/', FilterProductView.as_view(), name='filter'),
    path('products/search/', Search.as_view(), name='search'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail')
]