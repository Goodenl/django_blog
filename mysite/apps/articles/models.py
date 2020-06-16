import datetime
from django.db import models
from django.utils import timezone

class Article(models.Model):
	""" models Articles for post; have author, title, text and pub_date """
	article_author = models.CharField('автор статьи', max_length = 100)
	article_title = models.CharField('название статьи', max_length = 100)
	article_text = models.TextField('текст статьи')
	article_rating = models.IntegerField('рейтинг статьи', default=0)
	article_tags = models.BooleanField(default=True, null=True, blank=True)

	no_public = models.BooleanField(default=True)

	pub_date = models.DateTimeField('дата публикации статьи', default=timezone.now)


	def __str__(self):
		return self.article_title

	def was_published_recently(self):
		return self.pub_date >= (timezone.now() - datetime.timedelta(days = 7))

	class Meta:
		verbose_name = 'Статья'
		verbose_name_plural = 'Статьи'

class Comment(models.Model):
	""" models Comments for Articles; have author, text and pub_date """
	article = models.ForeignKey(Article, on_delete = models.CASCADE)

	comment_author = models.CharField('автор комментария', max_length = 100)
	comment_text = models.CharField('текст комментария', max_length = 255)
	pub_date = models.DateTimeField('дата публикации комментария', default=timezone.now)

	def __str__(self):
		return self.comment_author

	class Meta:
		verbose_name = 'Комментарий'
		verbose_name_plural = 'Комментарии'