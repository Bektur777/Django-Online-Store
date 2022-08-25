from django.shortcuts import render, redirect

from django.views.decorators.http import require_POST
from .models import *
from cart.views import delete_goods


def make_order(request):
    return render(request, 'store/ordering.html')


@require_POST
def order(request):
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    email = request.POST.get('email')
    address = request.POST.get('address')
    city = request.POST.get('city')
    phone = request.POST.get('phone')

    make_order = Order.objects.create(user=request.user, first_name=first_name, last_name=last_name,
                                 email=email, address=address, city=city, phone=phone)

    quantity = 1
    for i in request.session.get('goods'):
        for j in i.values():
            product = Product.objects.get(pk=j)
            price = product.price
            item = OrderItem.objects.create(order=make_order, product=product, price=price, quantity=quantity)
            del request.session['goods']

    return redirect('order:get_orders')


def get_order(request):
    orders = OrderItem.objects.all().order_by('-order__created')
    return render(request, 'store/order_list.html', context={'orders': orders})
