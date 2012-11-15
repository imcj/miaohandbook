#!/usr/bin/env python
#! -*- encoding:utf-8 -*-

from django import forms
from handbook.models import Cat

class CatModelForm ( forms.ModelForm ):
	summary = forms.CharField ( widget = forms.Textarea )

	class Meta:
		model = Cat