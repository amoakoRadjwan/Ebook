from django.db import models
from django.contrib import admin
class Book(models.Model):
	title=models.CharField(max_length=200)
	author=models.CharField(max_length=200)
	def __unicode__(self):
		return self.title

class UploadModel(models.Model):
	file = models.FileField(upload_to='home/aiti /Desktop/')
     	date_uploaded=models.DateTimeField('date uploaded')
	upload_title = models.CharField(max_length=50)
	uplaod_author=models.CharField(max_length=50)
	def __unicode__(self):
		return self.upload_title


class Search(models.Model):
    	search_title=models.ForeignKey(Book)
    	search_author=models.CharField(max_length=200)    
	def __unicode__(self):
		return self.search_author


admin.site.register(Search)
admin.site.register(Book)
admin.site.register(UploadModel)
# Create your models here.
