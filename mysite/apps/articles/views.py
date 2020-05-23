from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import Http404

from .models import Article
from .forms import ArticleForm
from django.db.models import Max

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

class ArticleListView(ListView):
	model = Article
	template_name = "articles/list.html"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)

		context['articles_list'] = Article.objects.order_by("-id")

		max_rating = Article.objects.all().aggregate(Max('article_rating'))

		context['max_rating'] = max_rating["article_rating__max"]

		return context

class DetailListView(DetailView):
	model = Article
	template_name = "articles/detail.html"
	context_object_name = "article"

def leave_comment(request, pk):
	try:
		a = Article.objects.get( id = pk )	# get Article by Id
	except:
		raise Http404("Статья не найдена!")

	a.comment_set.create(comment_author = request.POST['author'], comment_text = request.POST['comment']) # create and add comment
	return redirect('articles:detail', pk = a.id)

class RedirectSuccessMixin():

	def get_success_url(self):
		return '%s?id=%s' % (self.success_url, self.object.id)

class ArticleCreateView(CreateView):
	model = Article
	template_name = "articles/create_article.html"
	form_class = ArticleForm
	success_url = reverse_lazy('articles:articles')

class ArticleUpdateView(RedirectSuccessMixin, UpdateView):
	model = Article
	template_name = "articles/create_article.html"
	form_class = ArticleForm
	success_url = reverse_lazy("articles:articles")

	def get_context_data(self, **kwargs):
		kwargs['update'] = True
		return super().get_context_data(**kwargs)

class ArticleDeleteView(DeleteView):
	model = Article
	template_name = "articles/create_article.html"
	success_url = reverse_lazy("articles:articles")

# def update_article(request, pk):

# 	get_article = Article.objects.get(pk=pk)	# get Article by send url argument(pk)
# 	success_update = False						# success make form update

# 	if request.method == 'POST':
# 		form = ArticleForm(request.POST, instance=get_article)
# 		if form.is_valid():
# 			form.save()
# 			success_update = True

# 	if success_update:
# 		return redirect('articles:detail', pk = get_article.id)
# 	else:

# 		template = "articles/create_article.html"

# 		context = {
# 			"get_article": get_article,
# 			"update": True,
# 			"form": ArticleForm(instance=get_article),
# 		}

# 		return render(request, template, context)