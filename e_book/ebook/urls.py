from django.conf.urls.defaults import *
from django.contrib import admin

urlpatterns = patterns('',
	url(r'^$', 'ebook.views.book_list'),
	url(r'^base/(\d+)?$', 'ebook.views.book_list'),
	url(r'^(detail|info)/(?P<id>\d+)/((?P<showFile>.*)/)?$', 'ebook.views.book_detail'),

	#url(r'^search/(\w+)*$', 'ebook.views.blog_search'),
	
	
)
	#
