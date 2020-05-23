from django.urls import path

from . import views

app_name = 'glagna'
urlpatterns = [
	path("", views.LoginUserView.as_view(), name = 'index'),
]