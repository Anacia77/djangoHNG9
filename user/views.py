from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse


from .forms import CreateUserForm, User, DetailForm

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .decorators import unauthenticated_user, allowed_users
#using email
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string

from django.views.decorators.csrf import csrf_exempt


from django.views.generic import View
from django.template.loader import get_template
from .reportPDF import render_to_pdf







# Create your views here.
@login_required(login_url= 'user:login')
def welcomePage(request):
    
    return render(request, 'site/home.html')



@login_required(login_url= 'user:login')
#@allowed_users(allowed_roles=['admin', 'staff', 'user'])
def account(request):
    form = DetailForm() 
    if not request.user.is_authenticated:  #if the user is not authenticated
        return redirect('user:login')
    else:
    
        #if request.method == 'POST':
            #form = DetailForm(request.POST, request.FILES)
            #if form.is_valid():
                #form.save()

        return render(request, 'site/account.html', {'form': form})

def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            messages.success(request, f'Account registration successful for {user}.')
            form.save()
            return redirect('user:login')

    context = {'form': form}
    return render(request, 'site/reg.html', context)
    #return render(request, 'site/register.html', context)
    #return render(request, 'site/regForm.html', context)

@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, username=username, email=email, password=password)
        #user= EmailBackEnd.authenticate(request, request.POST.get('email'), request.POST.get('password'))
        if user is not None:
            login(request, user)
            return redirect('user:account')
        else:
            messages.info(request, 'Username or Password is incorrect')
    
    return render(request, 'site/index.html')
    #return render(request, 'site/login.html')


def logoutUser(request):
    logout(request)
    return redirect('user:login')

@login_required(login_url= 'user:login')
#@allowed_users(allowed_roles=['admin', 'staff', 'user'])
def account_settings(request):
    detail = request.user.detail
    form = DetailForm(instance=detail)

    if request.method == 'POST':
        form = DetailForm(request.POST, request.FILES, instance=detail)
        if form.is_valid():
            form.save()
            messages.success(request,"Account updated successfully")
        else:
            messages.error(request,"Failed to update")
    return render(request, 'site/account_settings.html', {'form': form})


@csrf_exempt
def check_email_exist(request):
    email=request.POST.get("email")
    user_obj=User.objects.filter(email=email).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

@csrf_exempt
def check_username_exist(request):
    username=request.POST.get("username")
    user_obj=User.objects.filter(username=username).exists()
    if user_obj:
        return HttpResponse(True)
    else:
        return HttpResponse(False)

def user_profile(request):
    return render(request,"site/changePass.html")

def user_profile_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("user:user_profile"))
    else:
        #first_name=request.POST.get("first_name")
        #last_name=request.POST.get("last_name")
        password=request.POST.get("password")
        try:
            userdetail=User.objects.get(id=request.user.id)
            #user.first_name=first_name
            #user.last_name=last_name
            if password!=None and password!="":
                userdetail.set_password(password)
            userdetail.save()
            messages.success(request, "Successfully Updated Profile")
            return HttpResponseRedirect(reverse("user:user_profile"))
        except:
            messages.error(request, "Failed to Update Profile")
            return HttpResponseRedirect(reverse("user:user_profile"))

