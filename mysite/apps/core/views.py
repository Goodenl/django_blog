from django.shortcuts import render
from django.urls import reverse_lazy

from django.views.generic.edit import CreateView

from django.contrib.auth.views import LogoutView, LoginView
from django.contrib.auth.models import User

from .forms import AuthUserForm, SignUpForm

class LoginUser(LoginView):
	form_class = AuthUserForm

class LogoutUser(LogoutView):
	next_page = reverse_lazy("glagna:index")

class SignUpUser(CreateView):
	form_class = SignUpForm
	success_url = reverse_lazy('glagna:index')
	template_name = 'core/register_user.html'