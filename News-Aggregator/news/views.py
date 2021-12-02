import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup as BSoup
from news.models import Headline

requests.packages.urllib3.disable_warnings()

def index(request):
	if request.user.is_authenticated():
		return render(request, "news/index.html")
	else:
		return render(request, "news/login.html")

def news_list(request):
	headlines = Headline.objects.all()[::-1]
	context = {
		'object_list': headlines,
	}
	return render(request, "news/home.html", context)

def scrape(request):
	session = requests.Session()
	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
	# url = "https://www.theonion.com/"
	url = "https://timesofindia.indiatimes.com/"

	content = session.get(url, verify=False).content
	soup = BSoup(content, "html.parser")
	News = soup.find_all('figure', {"class":"_1Fkp2"})
	for artcile in News:
		main = artcile.find_all('a')[0]
		link = main['href']
		image_src = str(main.find('img')['src'])
		# title = main['title']
		title = 'test'
		new_headline = Headline()
		new_headline.title = title
		new_headline.url = link
		new_headline.image = image_src
		new_headline.save()
	return redirect("../")

