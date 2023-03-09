import requests
import wikipedia
import pywhatkit as kit
from email.message import EmailMessage
import smtplib
from decouple import config
import os

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def play_on_youtube(video):
    kit.playonyt(video)

def search_on_google(query):
    kit.search(query)

def send_whatsapp_message(number, message):
    kit.sendwhatmsg_instantly(f"+91{number}", message)

# TMDB_API_KEY = config('TMDB_API_KEY', cast=str)
# def get_trending_movies():
#     trending_movies = []
#     res =requests.get(
#         f"https://api.themoviedb.org/3/trending/movie/day?api_key={TMDB_API_KEY}").json()
#     results = res["results"]
#     for r in results:
#         trending_movies.append(r["original_title"])
#     return trending_movies[:5]

# NEWS_API_KEY = config('NEWS_API_KEY', cast=str)
# def get_latest_news():
#     news_headlines = []
#     res = requests.get(
#         f"https://newsapi.org/v2/top-headlines?country=in&apiKey={os.environ['NEWS_API_KEY']}&category=general").json()
#     articles = res["articles"]
#     for article in articles:
#         news_headlines.append(article["title"])
#     return news_headlines[:5]

def get_random_joke():
    headers = {
        'Accept': 'application/json'
    }
    res = requests.get("https://icanhazdadjoke.com/", headers=headers).json()
    return res["joke"]

def get_random_advice():
    res = requests.get("https://api.adviceslip.com/advice").json()
    return res['slip']['advice']