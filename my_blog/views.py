from django.shortcuts import render
from django.shortcuts import render_to_response
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse


from .models import Blog, Category


def index(request):
	return render_to_response('index.html', {
		'categories': Category.objects.all(),
		'posts': Blog.objects.all()[:7:-1]
		})

def view_post(request, slug):
	return render_to_response('view_post.html', {
		'post':get_object_or_404(Blog, slug=slug)
		})

def view_category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	return render_to_response('view_category.html', {
		'category': category,
		'posts': Blog.objects.filter(category=
										category)[:7]
		})

