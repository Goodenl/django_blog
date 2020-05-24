from django.views.generic import TemplateView
import requests
from bs4 import BeautifulSoup as BS

class NewsMainViews(TemplateView):
	template_name = "news/news-main.html"

	def get_context_data(self, *args, **kwargs):
		context = super().get_context_data(*args, **kwargs)
		print('gg')
		r = requests.get('https://pikabu.ru/')

		bs = BS(r.content, 'html.parser')

		news_post = []

		for i in range(12):
			text_raw = bs.select('.story__title > a')[i].text
			news_post.append(text_raw)

		context['news_post'] = news_post
		return context