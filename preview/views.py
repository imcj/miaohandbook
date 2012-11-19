from django.shortcuts import render_to_response, render
from handbook.models import Cat, CatPhoto

def home ( request ):
	return render (
		request,
		"preview/home.html",
		{ }
	)

def detail ( request ):
	return render (
		request,
		"preview/detail.html",
		{ }
	)