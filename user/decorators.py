from django.http import HttpResponse
from django.shortcuts import redirect

# Once user is logged into an account, this prevents another user from logging in the same page.
def unauthenticated_user(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('user:account')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func


def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper_func(request, *args, **kwargs):

            print('Working', allowed_roles)
            return view_func(request, *args, **kwargs)
        return wrapper_func
    return decorator