from django.db import models

# Create your models here.
class index_text(models.Model):
	otsi_midagi = models.CharField(max_length=999)
	loosung = models.CharField(max_length=999)

class contact(models.Model):
	phone = models.CharField(max_length=999)
	email = models.CharField(max_length=999)
	address = models.CharField(max_length=999)

class misc(models.Model):
	title = models.CharField(max_length=999,blank=True)
	desc = models.TextField(blank=True)
	keywords = models.CharField(max_length=999,blank=True)
	author = models.CharField(max_length=999,blank=True)