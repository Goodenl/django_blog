from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from .forms import AuthUserForm

from django.urls import reverse_lazy

class LoginUserView(LoginView):
	model = User
	template_name = "glagna/index.html"
	form_class = AuthUserForm