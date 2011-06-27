from django.db import models

class Book(models.Model):
	title=models.CharField(max_length=200)
	author=models.CharField(max_length=200)
	def __unicode__(self):
		return self.title

class UploadModel(models.Model):
	file = models.FileField(upload_to='home/aiti/Desktop/')
     	date_uploaded=models.DateTimeField('date uploaded')
	def __unicode__(self):
		return self.file


class Search(models.Model):
    	search_title=models.ForeignKey(Book)
    	search_author=models.CharField(max_length=200)    
	def __unicode__(self):
		return self.search_title
# Create your models here.
