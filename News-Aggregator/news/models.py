from django.conf import settings
from django.db import models

# Create your models here.

class Headline(models.Model):
	title = models.CharField(max_length=200)
	image_src = models.URLField(null=True, blank=True)
	source = models.URLField(null=False, blank=False)
	channel = models.CharField(max_length=30)
	channel_short = models.CharField(max_length=30)

	def __str__(self):
		return self.title

class User(models.Model):
	username = models.CharField(max_length=15, blank=False, null=False)
	email = models.EmailField(primary_key=True, blank=False, null=False, unique=True)
	password = models.CharField(max_length=20, blank=False, null=False)
	favourite_paper = models.TextField(blank=True,null=True)
