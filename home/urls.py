from django.contrib import admin
from django.contrib.auth.forms import AuthenticationForm
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .forms import LoginForm

urlpatterns = [
    path("",views.index,name='home'),
    path("about/",views.about,name='home'),
    path("service/",views.service,name='home'),
    path("contact/",views.contact,name='home'),
    path("register/",views.CustomerRegistrationView.as_view(),name='customerregistration'),
    path("login/", auth_views.LoginView.as_view(template_name='login.html', authentication_form=LoginForm), name='login'),
    path("accounts/profile/",views.profile,name='home')
    ]
    