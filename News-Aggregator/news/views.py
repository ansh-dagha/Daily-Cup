import requests, json
from django.shortcuts import render, redirect
from news.models import User, Headline
from news.forms import LoginForm
from datetime import datetime, timedelta
from news.utilities import *
requests.packages.urllib3.disable_warnings()

current_date = datetime.date(datetime.now()-timedelta(1))

def scrape():
	Headline.objects.all().delete()
	get_news_from_toi()
	get_news_from_cnn()
	get_news_from_news18()
	get_news_from_ht()

def index(request):
	global current_date
	today = datetime.date(datetime.now())
	if today > current_date:
		print('Update DB')
		scrape()
		current_date = today
	headlines = Headline.objects.order_by('?').all()
	data = {'headlines':headlines}
	return render(request, "news/index.html",data)

def today(request):
	interested_news = json.loads(User.objects.get(email=request.session['email']).favourite_paper)
	headlines = Headline.objects.order_by('?').all()
	data = {'interested_news':interested_news, 'headlines':headlines}
	return render(request, "news/index.html", data)

def signout(request):
	request.session.clear()
	request.session['logged_in'] = False
	return redirect('/')

def login(request):
	form = LoginForm()
	err=''
	if request.method == 'POST':
		email = request.POST.get('email')
		password = request.POST.get('password')
		try:
			user_obj = User.objects.get(email=email)
			if user_obj.email== email and user_obj.password == password:
				request.session['logged_in'] = True
				request.session['email'] = email
				return redirect('/')
		except:
			err='Invalid Credentials!'
	context = {'form':form, 'err':err}
	return render(request, "news/login.html",context)

def signup(request):
	err=''
	if request.method == 'POST':
		username = request.POST.get('username')
		email = request.POST.get('email')
		password = request.POST.get('password')
		interested_news = request.POST.getlist('interested_news')
		try:
			User.objects.create(username = username,
								email = email,
								password = password,
								feed_date = datetime.date(datetime.now()-timedelta(1)),
								favourite_paper= json.dumps(interested_news)).save()
		except:
			err='Email Already Exists!'
			data = {'err':err}
			return render(request, "news/signup.html", data)
		request.session['logged_in'] = True
		return redirect('/')
	data = {'err':err}
	return render(request, "news/signup.html", data)

def getallnews(request):
	pass

def aboutus(request):
	return render(request,"news/about.html")