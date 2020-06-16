from django import forms

from .models import Article


class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ('article_author', 'article_title', 'article_text')

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		for field in self.fields:
			self.fields[field].widget.attrs['class'] = 'form-control'
			self.fields[field].label = ''

		self.fields['article_author'].widget.attrs['type'] = 'hidden'

		self.fields['article_title'].widget.attrs['class'] = 'form-control mx-auto'

		self.fields['article_text'].widget.attrs['class'] = 'form-control mx-auto'
		self.fields['article_text'].widget.attrs['id'] = 'article_text_create'

		self.fields['article_title'].widget.attrs['placeholder'] = 'Article Title'
		self.fields['article_tags'].widget.attrs['placeholder'] = 'Article Tags'
		self.fields['article_text'].widget.attrs['placeholder'] = 'Article Text'