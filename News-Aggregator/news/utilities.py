import requests, json
from bs4 import BeautifulSoup as BSoup
from news.models import Headline
import random

def random_images_18():
    news18_photos = ['static/news/images/blank_news18.jpg',
    'static/news/images/blank_news18_1.jpg',
    'static/news/images/blank_news18_2.jpg',
    ]

    return random.choice(news18_photos)

def random_images_toi():
    toi_photos = ['static/news/images/blank_image.jpg',
    'static/news/images/blank_toi.jpg',
    'static/news/images/blank_toi_2.jpg',
    ]

    return random.choice(toi_photos)


def get_news_from_toi():
    url = "https://timesofindia.indiatimes.com/"
    page = requests.get(url)
    soup = BSoup(page.content, 'html.parser')
    news = soup.find_all('figure', {"class":"_1Fkp2"})
    articles_db = []
    channel = 'Times of India'
    length = min(20,len(news))
    for article in news[0:length]:
        headline = article.figcaption.getText()
        source = article.find('a', {"class":"_3SqZy"})['href']
        Headline.objects.create(title=headline, image_src=random_images_toi(), source=source, channel=channel, channel_short='times-of-india').save()

def get_news_from_cnn():
    articles_db = []
    url = "https://search.api.cnn.io/content?q=coronavirus&sort=newest&category=business,us,politics,world,opinion,health&size=100&from={}"
    channel = 'CNN'
    with requests.Session() as req:
        for item in range(1, 3):
            r = req.get(url.format(item)).json()
            length = min(20,len(r['result']))
            for a in r['result'][0:length]:
                Headline.objects.create(title=a['headline'], image_src=a['thumbnail'], source=a['url'], channel=channel, channel_short='cnn').save()

def get_news_from_news18():
    url = "https://www.news18.com/"
    reponse = requests.get(url)
    articles_db= []
    channel = 'News 18'
    if reponse.ok:
        soup = BSoup(reponse.content, 'html.parser')
        News = soup.find_all('li', {"class":"fnt_siz_e"})
        length = min(20,len(News))
        for artcile in News[0:length]:
            main = artcile.find_all('a')[0]
            link = main['href']
            title = main['title']
            Headline.objects.create(title=title, image_src=random_images_18(), source=link, channel=channel, channel_short='news-18').save()

def get_news_from_ht():
    session = requests.Session()
    session.headers = {"User-Agent": "Googlebot/2.1 (+http://www.google.com/bot.html)"}
    url = 'https://www.hindustantimes.com/'
    content = session.get(url, verify=False).content
    soup = BSoup(content, "html.parser")
    articles_db=[]
    News = soup.find_all('div', {"class":"cartHolder"})
    channel = 'Hindustan Times'
    length = min(20,len(News))
    for article in News[0:length]:
        main = article.find_all('a')[1]
        source = 'https://www.hindustantimes.com' + main['href']
        image_src = article.find_all('img')[0]['src']
        title = main.get_text()
        Headline.objects.create(title=title, image_src=image_src, source=source, channel=channel, channel_short='hindustan-times').save()