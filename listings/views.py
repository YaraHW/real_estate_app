from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render, get_object_or_404
from .models import Listing
from .choices import price_choices, bedroom_choices, state_choices


# Create your views here.
def index(request):
	listings = Listing.objects.order_by('-list_date').filter(is_published=True) # получит все переменные из класса Listing в моделс
	paginator = Paginator(listings,6)
	page = request.GET.get('page')
	paged_listings = paginator.get_page(page)
	# создадим переменную со словарем куда будем передавать данные
	context = {
		'listings':paged_listings
	}
	return render(request, 'listings/listings.html', context)

def listing(request, listing_id): # listing_id передаем из urls.py чтоб кнопка more info на странице под домами вела на конкретный дом
	listing = get_object_or_404(Listing, pk=listing_id)
	context = {
		'listing':listing
	}
	return render(request, 'listings/listing.html', context)

def search(request):
	queryset_list = Listing.objects.order_by('-list_date')
	#Keywords - поиск по ключевым словам
	if 'keywords' in request.GET:
		keywords = request.GET['keywords']
		if keywords:
			queryset_list = queryset_list.filter(description__icontains=keywords)
	#City - поиск по городу
	if 'city' in request.GET:
		city = request.GET['city']
		if city:
			queryset_list = queryset_list.filter(city__iexact=city)# iexact - case insencitive поиск, но надо правильно ввести город
	# state - поиск по штату
	if 'state' in request.GET:
		state = request.GET['state']
		if state:
			queryset_list = queryset_list.filter(state__iexact=state)
	# bedrooms - поиск по спальным комнатам
	if 'bedrooms' in request.GET:
		bedrooms = request.GET['bedrooms']
		if bedrooms:
			queryset_list = queryset_list.filter(bedrooms__lte=bedrooms) # lte - вплоть до указанного значения( допустим вбил 3, получу 1,2,3)
	# price - поиск по цене
	if 'price' in request.GET:
		price = request.GET['price']
		if price:
			queryset_list = queryset_list.filter(price__lte=price)  # lte - вплоть до указанного значения( допустим вбил 3, получу 1,2,3)
	context = {
		'state_choices': state_choices,  # из файла listings/choices закинули в словарь чтоб в шаблоне не указывать
		'bedroom_choices': bedroom_choices,  # из файла listings/choices закинули в словарь чтоб в шаблоне не указывать
		'price_choices': price_choices,  # из файла listings/choices закинули в словарь чтоб в шаблоне не указывать
		'listings' : queryset_list,
		'values' : request.GET # чтоб в поиске при вводе данных оставались значения
	}
	return render(request, 'listings/search.html', context)