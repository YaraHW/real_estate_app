from django.contrib import admin
from .models import Realtor
# Register your models here.

"""Where we can customize admin stuff for realtors app"""
""" Тоже самое что и в admin.py в приложении listings"""
class RealtorAdmin(admin.ModelAdmin):
	list_display = ('id','name','email','hire_date')
	list_display_links = ('id','name')
	search_fields = ('name',)
	list_per_page = 25

admin.site.register(Realtor, RealtorAdmin) # создали вкладку Realtor со всеми параметрами указанными в классе Realtor в models в админке джанго