from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Albums(models.Model):
	album_type=models.CharField(max_length=200)
	