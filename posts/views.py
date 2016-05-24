from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

#Para hacer las queries de las bbdd
from posts.models import Post


# Create your views here.
def post_create(request):
	context = {
		"title": "Create"
	}
	return render (request, "index.html",context)

def post_detail(request): #retrive
	#instance = Post.objects.get(id=300)  ¡Mejor la línea de abajo para controlar el error si no existe!
	instance = get_object_or_404(Post, id=3)
	context = {
		"title": instance.title,
		"instance": instance,
	}
	return render (request, "post_detail.html",context)

def post_list(request):  #list items
	if request.user.is_authenticated():
		queryset = Post.objects.all()
		context = {
			"object_list": queryset,
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
