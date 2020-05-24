from django.urls import path

from . import views

app_name = 'glagna'
urlpatterns = [
	path("", views.GlagnaIndexView.as_view(), name = 'index'),
]