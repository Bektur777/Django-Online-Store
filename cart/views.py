from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


@require_POST
def add_to_cart(request, id):
    if not request.session.get('goods'):
        request.session['goods'] = list()
    else:
        request.session['goods'] = list(request.session['goods'])

    add_data = {
        'type': request.POST.get('type'),
        'id': id,
    }

    request.session['goods'].append(add_data)
    request.session.modified = True
    return redirect(request.POST.get('url_from'))


@require_POST
def remove_from_cart(request, id):
    for item in request.session['goods']:
        if item['id'] == id and item['type'] == request.POST.get('type'):
            item.clear()

    while {} in request.session['goods']:
        request.session['goods'].remove({})

    if not request.session['goods']:
        del request.session['goods']

    request.session.modified = True

    return redirect(request.POST.get('url_from'))


def delete_goods(request):
    if request.session.get('goods'):
        del request.session['goods']

    return redirect(request.POST.get('url_from'))

