from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def post_create(request):
	context = {
		"title": "Create"
	}
	return render (request, "index.html",context)

def post_detail(request): #retrive
	context = {
		"title": "Detail"
	}
	return render (request, "index.html",context)

def post_list(request):  #list items
	if request.user.is_authenticated():
		context = {
			"title": "My user List"
		}
	else:
		context = {
			"title": "List"
		}
	return render (request, "index.html",context)
	#return HttpResponse("<h1>List</h1>")

def post_update(request):
	context = {
		"title": "Update"
	}
	return render (request, "index.html",context)

def post_delete(request):
	context  = {
		"title": "Delete"
	}
	return render (request, "index.html",context)
