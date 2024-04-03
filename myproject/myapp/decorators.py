# myapp/decorators.py
import functools
from django.http import JsonResponse
from firebase_admin import auth as firebase_auth

def firebase_login_required(view_func):
    @functools.wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        auth_header = request.headers.get('Authorization')
        if not auth_header or not auth_header.startswith('Bearer '):
            return JsonResponse({'error': 'No Firebase ID token provided.'}, status=401)
        
        id_token = auth_header.split('Bearer ')[1]
        try:
            decoded_token = firebase_auth.verify_id_token(id_token)
            request.user_id = decoded_token['uid']
            return view_func(request, *args, **kwargs)
        except ValueError as e:
            return JsonResponse({'error': str(e)}, status=401)
    
    return _wrapped_view