from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),

	url(r'^my_blog/view/(?P<slug>[^\.]+).html',
			views.view_post, name='view_blog_post'),

	url(r'^my_blog/(?P<slug>[^\.]+).html',
			views.view_category, name='view_blog_category')

]