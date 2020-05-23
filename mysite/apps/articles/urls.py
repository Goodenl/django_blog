from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
	path("", views.ArticleListView.as_view(), name = 'articles'),
	path("post_<int:pk>/", views.DetailListView.as_view(), name = 'detail'),
	path("post_<int:pk>/leave_comment/", views.leave_comment, name = 'leave_comment'),
	
	path("create_article/", views.ArticleCreateView.as_view(), name = 'create_article'),
	path("update_article/<int:pk>", views.ArticleUpdateView.as_view(), name = 'update_article'),
	path("delete_article/<int:pk>", views.ArticleDeleteView.as_view(), name = 'delete_article'),

]