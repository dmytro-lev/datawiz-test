from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . import datawiz_auth
from . import datawiz
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from pprint import pprint
# Create your views here.
def index(request):
    if request.method == "POST":
        print('login form')
        email = request.POST['email']
        password = request.POST['password']

        try:
            user_datawiz = datawiz_auth.Auth(email,password)
            print(user_datawiz)

        except:
            return HttpResponse('Wrong credentials')

        user, created = User.objects.get_or_create(username=email, email=password)
        if created:
            user.set_password(password)  # This line will hash the password

            user.save()  # DO NOT FORGET THIS LINE

        login(request, user)
        return redirect('/')

    else:
        if request.user.is_authenticated:
            return render(request, 'statistic/index.html')
        else:
            return render(request, 'statistic/login.html')

@login_required
def logout_my(request):
    logout(request)
    return redirect('/')

@login_required
def get_client_info(request):
    if request.method == "POST":
        username = request.user.username
        user = User.objects.get(username=username)

        dw = datawiz.DW(user, user.email)
        result = dw.get_client_info()
        return JsonResponse({'result':result})
    else:
        return redirect('/')

@login_required
def get_main(request):
    return HttpResponse('main')
