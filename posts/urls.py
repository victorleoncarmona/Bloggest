#redirección para vistas de posts
from django.conf.urls import url
from django.contrib import admin

#Importamos nuestra aplicación como indica las indicaciones del fichero principal
"""
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
"""

from .views import (
	post_list,
	post_create,
	post_detail,
	post_update,
	post_delete,
	)

urlpatterns = [
	url(r'^$', post_list, name='post_list'),
    url(r'^create/$', post_create, name='post_create'),
    url(r'^detail/$', post_detail, name='post_detail'),
    url(r'^update$', post_update, name='post_update'),
    url(r'^delete$', post_delete, name='post_delete'),
]
