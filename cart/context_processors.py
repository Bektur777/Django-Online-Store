from operator import length_hint


def get_len(request):
    return {'count': length_hint(request.session.get('goods'))}
