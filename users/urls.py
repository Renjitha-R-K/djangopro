"""
URL configuration for careerhub project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path,reverse_lazy
from users import views
from django.contrib.auth.views import LoginView,LogoutView,PasswordResetView,PasswordResetDoneView,PasswordResetCompleteView,PasswordResetConfirmView
app_name="users"
urlpatterns = [
    path('',views.HomeView.as_view(),name='home'),
    path('register/',views.RegisterView.as_view(),name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(),name='logout'),
    path('password-change/',views.CustomPasswordChangeView.as_view(),name='password-change'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password-done'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(), name="password-complete"),
    path('password-reset/confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(success_url=reverse_lazy('users:password-complete')), name="password-confirm"),
    path('password-reset/',PasswordResetView.as_view(success_url=reverse_lazy('users:password-done')),name='password-reset'),

]
