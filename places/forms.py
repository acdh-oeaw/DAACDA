# -*- coding: utf-8 -*-
from autocomplete_light import shortcuts as al
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.forms import ModelForm

from .autocomplete_light_registry import NameAutocomplete
from labels.models import Label
from .models import Place

class PlaceForm(al.ModelForm):
	class Meta:
		model = Place
		fields = ['name', 'alternative_name', 'geonames_id', 'lat', 'lng']

	def __init__(self, *args, **kwargs):
		super(PlaceForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper()
		self.helper.form_tag = False