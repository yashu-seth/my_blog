from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class Blog(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)
	body = models.TextField()
	posted = models.DateTimeField(db_index=True, 
									auto_now_add=True)

	category = models.ForeignKey('my_blog.Category')

	@python_2_unicode_compatible
	def __str__(self):
		if len(self.title)>50:
			return self.title[:50]+'.....'
		return self.title


class Category(models.Model):
	title = models.CharField(max_length=100, unique=True)
	slug = models.SlugField(max_length=100, unique=True)

	@python_2_unicode_compatible
	def __str__(self):
		if len(self.title)>50:
			return self.title[:50]+'.....'
		return self.title