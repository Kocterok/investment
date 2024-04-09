from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('appINVEST.urls')),
    path('appauth/', include('appAuth.urls')),
]





# Для обеспечения аутентификации пользователей в вашем приложении на Django вы можете использовать встроенные средства аутентификации Django, такие как django.contrib.auth. Вот как вы можете настроить аутентификацию:

# Настройка URLs: Убедитесь, что у вас есть URL для входа (login), выхода (logout) и регистрации (register), если требуется. Вы можете добавить их в файл urls.py вашего приложения или проекта.

# Использование представлений для аутентификации: В Django есть встроенные представления для входа, выхода и регистрации. Вы можете использовать их, чтобы обеспечить соответствующий функционал. Например, django.contrib.auth.views.LoginView, django.contrib.auth.views.LogoutView, django.contrib.auth.views.RegisterView.

# Декораторы для проверки аутентификации: Вы можете использовать декоратор @login_required для представлений, которые требуют аутентификации пользователя. Это гарантирует, что пользователь будет перенаправлен на страницу входа, если он не аутентифицирован.

# Пример:

# # views.py

# from django.shortcuts import render, redirect
# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
# from django.contrib.auth import authenticate, login, logout

# def login_view(request):
#     if request.method == 'POST':
#         form = AuthenticationForm(request, request.POST)
#         if form.is_valid():
#             username = form.cleaned_data.get('username')
#             password = form.cleaned_data.get('password')
#             user = authenticate(username=username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('portfolio')
#     else:
#         form = AuthenticationForm()
#     return render(request, 'login.html', {'form': form})

# def logout_view(request):
#     logout(request)
#     return redirect('login')

# def register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return redirect('portfolio')
#     else:
#         form = UserCreationForm()
#     return render(request, 'register.html', {'form': form})

# @login_required
# def portfolio(request):
#     # Ваш код представления для портфеля
#     pass
# Шаблоны для входа, выхода и регистрации: Создайте соответствующие шаблоны для страниц входа, выхода и регистрации (login.html, logout.html, register.html), которые будут содержать формы для ввода информации и кнопки для отправки.

# Настройка параметров аутентификации: Вы можете настроить параметры аутентификации, такие как продолжительность сеанса, методы хеширования паролей и другие через файл настроек settings.py.

# Защита URL-адресов: Убедитесь, что ваши URL-адреса для страниц, требующих аутентификации, защищены соответствующим образом, например, с помощью декоратора @login_required.

# Это базовый пример того, как обеспечить аутентификацию пользователей в вашем приложении Django. Вы можете настроить его дальше в зависимости от требований вашего проекта.