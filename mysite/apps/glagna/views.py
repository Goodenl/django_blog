from django.contrib.auth.views import TemplateView, FormView

from articles.models import Article

from core.forms import AuthUserForm

from django.urls import reverse_lazy

class GlagnaIndexView(FormView):
	form_class = AuthUserForm
	template_name = "glagna/index.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(**kwargs)

		context['last_article'] = Article.objects.order_by("-pub_date")[:5]
		return context