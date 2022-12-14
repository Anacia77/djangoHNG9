from django.shortcuts import render, redirect
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def welcomePage(request):
    return render(request, 'site/home.html')

def userPage(request):
    return render(request, 'site/account.html')

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            messages.success(request, f'Account registration successful')
            form.save()
            return redirect('users:login')

    context = {'form': form}
    return render(request, 'site/register.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('users:account')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    return render(request, 'site/login.html')

def logoutUser(request):
    logout(request)
    return redirect('users:welcomePage')