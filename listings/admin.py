from django.contrib import admin
from .models import Listing
# Register your models here.

"""Where we can customize admin stuff for listings app"""
class ListingAdmin(admin.ModelAdmin):
	list_display = ('id','title','is_published','price','list_date','realtor') # в админке в приложении listing преобразует строку в список с этими параметрами
	list_display_links = ('id','title') # выбираем то, на что можно кликать в листингс
	list_filter = ('realtor',) # чтоб фильтровать по realtor
	list_editable = ('is_published',)
	search_fields = ('title','description','address','city','state','zipcode','price') # добавляет поиск по параметрам что в скобках
	list_per_page = 25

admin.site.register(Listing, ListingAdmin) # создали вкладку Listing со всеми параметрами указанными в классе Listing в models в админке джанго

