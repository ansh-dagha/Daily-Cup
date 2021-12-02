from django.urls import path
from news.views import index, login, signup, signout

app_name = 'news'
urlpatterns = [
	path('', index, name="index"),
	path('login', login, name="login"),
	path('signup', signup, name="signup"),
	path('signout', signout, name="signout"),
]