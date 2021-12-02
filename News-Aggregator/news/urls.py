from django.urls import path
from news.views import scrape, news_list

urlpatterns = [
	path('scrape/', scrape, name="scrape"),
	path('', index, name="index"),
]