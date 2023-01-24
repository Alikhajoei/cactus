from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError


class Genre(models.Model):
	name = models.CharField(max_length=300)
	icon = models.ImageField(upload_to='icons/', blank=True, null=True)
	slug = models.SlugField()


	def __str__(self):
		return self.name



class Book(models.Model):
	title = models.CharField(max_length=300)
	genre = models.ForeignKey(Genre,default="1" , on_delete=models.SET_DEFAULT)
	abstract = models.CharField(max_length=600 , blank=True , null=True)
	writer = models.CharField(max_length=100, blank=True, null=True)
	file = models.FileField(upload_to='pdfs/')
	user= models.ForeignKey(User,on_delete=models.CASCADE)
	def __str__(self):
		return self.title


class NewsEmail(models.Model):
	ip = models.CharField(max_length=40)
	email = models.EmailField(unique=True)
	joined_date = models.DateTimeField(default=timezone.now)

	def __str__(self):
		return self.email

