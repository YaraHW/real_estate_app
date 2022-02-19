from django.db import models
from datetime import datetime
from realtors.models import Realtor

"""Для создания таблицы в базе данных, после создания нужно создать миграции и применить их"""
# Create your models here.
class Listing(models.Model):
	"""Все это - поля класса(атрибуты класса) являются наследниками от models, в скобках есть обязательные параметры например max_length,
	либо же опциональные у всех, см доки джанго"""
	realtor = models.ForeignKey(Realtor, on_delete=models.DO_NOTHING)
	title  = models.CharField(max_length=200)
	address  = models.CharField(max_length=200)
	city  = models.CharField(max_length=100)
	state  = models.CharField(max_length=100)
	zipcode  = models.CharField(max_length=20)
	description  = models.TextField(blank=True) # blank значит что это поле опциональное
	price  = models.IntegerField()
	bedrooms  = models.IntegerField()
	bathrooms  = models.DecimalField(max_digits=2, decimal_places=1)
	garage  = models.IntegerField(default=0)
	sqft  = models.IntegerField()
	lot_size  = models.DecimalField(max_digits=5, decimal_places=1)
	photo_main  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_1  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_2  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_3  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_4  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_5  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	photo_6  = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
	is_published = models.BooleanField(default=True)
	list_date = models.DateTimeField(default=datetime.now, blank=True)
	def __str__(self):
		return self.title
