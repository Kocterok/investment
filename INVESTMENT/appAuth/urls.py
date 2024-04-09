from django.urls import path, include
from . import views


urlpatterns = [
    path('auth', views.AuthPage.as_view(), name="urlAuthPage"),
    path('', views.AccountPage.as_view(), name="urlAccountPage"),
    path('reg', views.RegPage.as_view(), name="urlRegPage"),
    path('logout', views.Logout.as_view(), name="urlLogout"),
]