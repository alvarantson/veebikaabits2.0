from django.db import models

# Create your models here.
class report(models.Model):
	app_name = models.CharField(max_length=999)
	search_item = models.CharField(max_length=999)
	date_time = models.CharField(max_length=999)
	misc = models.TextField(max_length=999)
	def __str__(self):
		return self.app_name+' - '+self.search_item+' - '+self.date_time


class browser_text(models.Model):
	show_filters = models.CharField(max_length=999)
	no_filter = models.CharField(max_length=999)
	price = models.CharField(max_length=999)
	low_to_high = models.CharField(max_length=999)
	high_to_low = models.CharField(max_length=999)
	name = models.CharField(max_length=999)
	a_to_z = models.CharField(max_length=999)
	z_to_a = models.CharField(max_length=999)
	okidoki = models.CharField(max_length=999)
	osta = models.CharField(max_length=999)
	soov = models.CharField(max_length=999)
	kuldnebors = models.CharField(max_length=999)

class blacklist(models.Model):
	words = models.TextField(max_length=9999)

class search_history(models.Model):
	search_item = models.CharField(max_length=999)
	time_elapsed = models.CharField(max_length=999)
	search_datetime = models.CharField(max_length=999)
	items_total = models.CharField(max_length=999)
	items_okidoki = models.CharField(max_length=999)
	items_osta = models.CharField(max_length=999)
	items_soov = models.CharField(max_length=999)
	items_kuldnebors = models.CharField(max_length=999)
	def __str__(self):
		return self.search_item+'('+self.items_total+') - '+self.time_elapsed+' #:'+self.search_datetime