from operator import length_hint

from store.models import Product


def get_len(request):
    request.session['quantity'] = length_hint(request.session.get('goods'))
    request.session.modified = True
    return {'count': request.session['quantity']}


def sum_goods(request):
    request.session['total_price'] = 0

    if request.session.get('goods') is None:
        pass
    else:
        for i in request.session.get('goods'):
            for j in i.values():
                product = Product.objects.get(pk=j)
                request.session['total_price'] += product.price

    return {'total_price': request.session['total_price']}
