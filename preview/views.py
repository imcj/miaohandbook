from django.shortcuts import render_to_response, render
from handbook.models import Cat, CatPhoto

def home ( request ):
	return render (
		request,
		"preview/home.html",
		{
			"cats": Cat.objects.all ()
		}
	)

def detail ( request, cat_id ):
	return render (
		request,
		"preview/detail.html",
		{
			"cat": Cat.objects.get ( id = cat_id ),
			"photos": CatPhoto.objects.filter ( cat = cat_id )
		}
	)

def gallery ( request, cat_id ):
	return render (
		request,
		"preview/gallery.html",
		{
			"cat": Cat.objects.get ( id = cat_id ),
			"photos": CatPhoto.objects.filter ( cat = cat_id )
		}
	)