from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.hashers import make_password        # шифрует пароли 
from django.http import HttpResponse
from django.contrib.auth.models import User                  # получает таблицу пользователя


class AuthPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('urlAccountPage')
        return render(request, 'appAuth/auth.html')
    def post(self, request):
        username = request.POST['login']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user != None:
            if user.is_active:
                login(request, user)
                return redirect('urlAccountPage')
            return HttpResponse("Вы заблокированы!")
        return HttpResponse("Такого пользователя нету!")
    
class AccountPage(View):
    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('urlAuthPage')
        return render(request, 'appAuth/account.html')
class RegPage(View):
    def get(self, request):
        if request.user.is_authenticated:
            return redirect('urlRegPage')
        return render(request, 'appAuth/reg.html')
    def post(self, request):
        username = request.POST['username']
        user = User.objects.filter(username=username)
        if not user.exists():                             # exists()  - булевое значение
            User.objects.create(
                username=username,
                last_name=request.POST['last_name'],            
                first_name=request.POST['first_name'],            
                password=make_password(request.POST['password']),            
            )
            return redirect('urlAuthPage')
        return HttpResponse("Такой ник есть!")
    
class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('urlAuthPage')   