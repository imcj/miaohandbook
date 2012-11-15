#!/usr/bin/env python
#! -*- encoding:utf-8 -*-

from django.contrib import admin
from handbook.models import Cat, CatPhoto
from handbook.forms import CatModelForm

class CatPhotoInline ( admin.TabularInline ):
	model = CatPhoto

class CatAdmin ( admin.ModelAdmin ):
	inlines = [
		CatPhotoInline,
	]
	form = CatModelForm

admin.site.register ( Cat, CatAdmin )