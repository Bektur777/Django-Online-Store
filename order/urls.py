from django.urls import path

from .views import *

app_name = 'order'
urlpatterns = [
    path('make_order/', make_order, name='make_order'),
    path('ordering/', order, name='order'),
    path('orders/', get_order, name='get_orders')
]
