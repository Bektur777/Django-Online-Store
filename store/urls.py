from django.urls import path
from .views import *

urlpatterns = [
    path('', StoreView.as_view(), name='store_view'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('products/', ProductView.as_view(), name='product_view'),
    path('products/filter/', FilterProductView.as_view(), name='filter'),
    path('products/search/', Search.as_view(), name='search'),
    path('products/<slug:slug>/', ProductDetailView.as_view(), name='product_detail'),
    path('cart/', cart, name='cart'),
    path('profile/', profile, name='profile')
]