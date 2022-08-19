from operator import length_hint

from store.models import Product


def get_len(request):
    request.session['quantity'] = length_hint(request.session.get('goods'))
    request.session.modified = True
    return {'count': request.session['quantity']}


def sum_goods(request):
    count = 0

    if request.session.get('goods') is None:
        pass
    else:
        for i in request.session.get('goods'):
            for j in i.values():
                product = Product.objects.get(pk=j)
                count += product.price

    return {'total_price': count}
