from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
	path("", views.index, name = 'index'),
	path("post_<int:article_id>/", views.detail, name = 'detail'),
	path("post_<int:article_id>/leave_comment/", views.leave_comment, name = 'leave_comment'),
	path("profiles_<int:profile_id>/", views.profiles, name = 'profiles'),
]