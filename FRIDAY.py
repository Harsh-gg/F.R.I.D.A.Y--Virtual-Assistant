import pyttsx3
import speech_recognition as sr
import os
import subprocess as sp
import requests
import wikipedia
from datetime import datetime
from random import choice
from utils import opening_text
from pprint import pprint
from online_ops import find_my_ip,get_trending_movies,play_on_youtube,search_on_google,send_whatsapp_message,get_random_joke,get_random_advice,get_weather_report


engine = pyttsx3.init('sapi5')

engine.setProperty('rate', 167)
engine.setProperty('volume', 1.0)

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def greet_user():    
    hour = datetime.now().hour
    if (hour >= 0) and (hour < 12):
        speak("Good Morning Sir")
    elif (hour >= 12) and (hour < 18):
        speak("Good afternoon Sir")
    else:
        speak("Good Evening Sir")
    speak("I am Friday. How may I assist you?")

def take_user_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print('Listening....')
        r.pause_threshold = 1
        audio = r.listen(source)
    try:
        print('Recognizing...')
        query = r.recognize_google(audio, language='en-in')
        if not 'exit' in query or 'stop' in query:
            speak(choice(opening_text))
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir, take care!")
            else:
                speak('Have a good day sir!')
            exit()
    except Exception:
        speak('Sorry, I could not understand. Could you please say that again?')
        query = 'None'
    return query


if __name__ == '__main__':
    greet_user()
    while True:
        query = take_user_input().lower()

        if 'open notepad' in query:
            codepath="C:\\Program Files\\Notepad++\\notepad++.exe"
            os.startfile(codepath)

        elif 'open discord' in query:
             codepath="C:\\Users\\gurna\\AppData\\Local\\Discord\\app-1.0.9011\\Discord.exe"
             os.startfile(codepath)

        elif 'open command prompt' in query or 'open cmd' in query:
             os.system('start cmd')

        elif 'open camera' in query:
            sp.run('start microsoft.windows.camera:', shell=True)

        elif 'open calculator' in query:
             codepath="C:\Windows\System32\calc.exe"
             os.startfile(codepath)
        
        elif 'open code editor' in query:
             codepath="C:\\Users\\gurna\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
             os.startfile(codepath)

        elif "what is my ip address" in query:
            ip_address = find_my_ip()
            speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen.')
            print(f'Your IP Address is {ip_address}')

        elif 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'play on youtube' in query:
            speak('What do you want to play on Youtube ?')
            video = take_user_input().lower()
            play_on_youtube(video)

        elif 'search on google' in query:
            speak('What do you want to search on Google ?')
            query = take_user_input().lower()
            search_on_google(query)

        elif "send whatsapp message" in query:
            speak('On what number should I send the message sir? Please enter in the console: ')
            number = input("Enter the number: ")
            speak("What is the message sir?")
            message = take_user_input().lower()
            send_whatsapp_message(number, message)
            speak("I've sent the message sir.")

        elif 'tell me a joke' in query:
            speak(f"Hope you like this one sir")
            joke = get_random_joke()
            speak(joke)
            speak("For your convenience, I am printing it on the screen.")
            pprint(joke)

        elif "give me an advice" in query:
            speak(f"Here's an advice for you, sir")
            advice = get_random_advice()
            speak(advice)
            speak("For your convenience, I am printing it on the screen.")
            pprint(advice)

        elif "suggest movies" in query:
            speak(f"Some of the trending movies are: {get_trending_movies()}")
            speak("For your convenience, I am printing it on the screen.")
            print(*get_trending_movies(), sep='\n')

        elif "how is the weather" in query:
            ip_address = find_my_ip()
            city = requests.get(f"https://ipapi.co/{ip_address}/city/").text
            speak(f"Getting weather report for your city {city}")
            weather, temperature, feels_like = get_weather_report(city)
            speak(f"The current temperature is {temperature}, but it feels like {feels_like}")
            speak(f"Also, the weather report talks about {weather}")
            speak("For your convenience, I am printing it on the screen.")
            print(f"Description: {weather}\nTemperature: {temperature}\nFeels like: {feels_like}")
