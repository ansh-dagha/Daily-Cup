import requests, json
from django.shortcuts import render, redirect
from news.models import User
from news.forms import LoginForm
from django.contrib.auth import login, authenticate
requests.packages.urllib3.disable_warnings()

def index(request):
	return render(request, "news/index.html")

def login(request):
	form = LoginForm()
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		user_obj = User.objects.get(email=email).__dict__
		if user_obj:
			print(user_obj)
			if user_obj['email']== email and user_obj['password'] == password:
				print(True)
				request.session['logged_in'] = True
				return redirect('index')
	context = {'form':form}
	return render(request, "news/login.html",context)

def signup(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		interested_news = request.POST.getlist('interested_news')
		User.objects.create(username = username,
							email = email,
							password = password,
							favourite_paper= json.dumps(interested_news)).save()
		return redirect('/')
	return render(request, "news/signup.html")

# def news_list(request):
# 	headlines = Headline.objects.all()[::-1]
# 	context = {
# 		'object_list': headlines,
# 	}
# 	return render(request, "news/home.html", context)

# def scrape(request):
# 	session = requests.Session()
# 	session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
# 	# url = "https://www.theonion.com/"
# 	url = "https://timesofindia.indiatimes.com/"

# 	content = session.get(url, verify=False).content
# 	soup = BSoup(content, "html.parser")
# 	News = soup.find_all('figure', {"class":"_1Fkp2"})
# 	for artcile in News:
# 		main = artcile.find_all('a')[0]
# 		link = main['href']
# 		image_src = str(main.find('img')['src'])
# 		# title = main['title']
# 		title = 'test'
# 		new_headline = Headline()
# 		new_headline.title = title
# 		new_headline.url = link
# 		new_headline.image = image_src
# 		new_headline.save()
# 	return redirect("../")