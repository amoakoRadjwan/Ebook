from django.template import Context, loader
from django.http import HttpResponse
from django.template import Context, loader
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from models import UploadModel, Search, Book
from django.http import HttpResponse

def book_list(request):
	book_list = UploadModel.objects.all()
	
	
	#print type(book_list)
	#print book_list
	#return HttpResponse('going to give a list')
	a = loader.get_template('ebook/base.html')
	b = Context({'book_list':book_list})
	#print uploadmodel.upload_title	
	return HttpResponse(a.render(b))

def book_detail(request, id, showFile=False):
	book = UploadModel.objects.get(id=id)
	if showFile:
		mybooks = UploadModel.objects.filter(upload_title__id=id)
		print mybooks
	t = loader.get_template('ebook/detail.html')
	c = Context({'book':book, 'mybooks':mybooks})
	return HttpResponse(t.render(c))
