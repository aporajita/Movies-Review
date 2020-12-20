from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Viewer(models.Model):
	user = models.OneToOneField(
	    User, null=True, blank=True, on_delete=models.CASCADE)
	name = models.CharField(max_length=200, null=True)
	email = models.CharField(max_length=200)

	def __str__(self):
		return self.name


class Category(models.Model):
	category = models.CharField(max_length=200)

	def __str__(self):
		return self.category


class Movies(models.Model):
	title = models.CharField(max_length=200)
	descricptions = models.CharField(max_length=200)

	category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
	image = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.title
