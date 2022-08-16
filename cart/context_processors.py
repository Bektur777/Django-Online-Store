
def get_len(request):
    return {'count': len(request.session.get('goods'))}
