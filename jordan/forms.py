from __future__ import unicode_literals

from .models import Albums
from django.db import models 
from django import forms

class AlbumsForm(forms.ModelForm):
	class Meta:
		model = Albums 
		fields = '__all__'
		




