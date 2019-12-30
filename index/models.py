from django.db import models

# Create your models here.
class index_text(models.Model):
	otsi_midagi = models.CharField(max_length=999)
	loosung = models.CharField(max_length=999)

class contact(models.Model):
	phone = models.CharField(max_length=999)
	email = models.CharField(max_length=999)
	address = models.CharField(max_length=999)