from django.urls import path

from .views import *

urlpatterns = [
    path('add/<int:id>', add_to_cart, name='add'),
    path('remove/<int:id>', remove_from_cart, name='remove'),
    path('delete/', delete_goods, name='delete'),
]
