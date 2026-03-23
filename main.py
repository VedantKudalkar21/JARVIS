import speech_recognition as sr
import webbrowser
import pyttsx3
import requests
import google.generativeai as genai
import os
import subprocess
import webbrowser
import datetime
from datetime import datetime, timedelta
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
from dotenv import load_dotenv
import datetime
import cv2
import wikipedia
from datetime import datetime
from calendar_auth import authenticate_google
from datetime import timedelta
import calendar_auth
import pickle
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import dateparser
import pywhatkit
import datetime
import numpy as np 
import math
import time
from deep_translator import GoogleTranslator
import pyjokes
import pyautogui
import tkinter as tk
from tkinter import ttk
import threading
from Jarvis_gui import play_gif

def send_whatsapp_message():
    speak("Whom do you want to message? Say the phone number including country code.")
    phone_number = listen().strip().replace(" ", "")  # Remove spaces
     
    speak("What message would you like to send?")
    message = listen()
    
    # Get current time
    now = datetime.now()
    hours = now.hour
    minutes = now.minute + 2  # Schedule 2 minutes ahead to avoid errors

    try:
        pywhatkit.sendwhatmsg(f"+{phone_number}", message, hours, minutes)
        speak(f"Message scheduled successfully to {phone_number}.")
    except Exception as e:
        speak("I couldn't send the message. Please try again.")
        print(f"Error: {e}")

SCOPES = ["https://www.googleapis.com/auth/calendar"]
def authenticate_google():
    creds = None

    # Load credentials from token.pickle if it exists
    if os.path.exists("token.pickle"):
        with open("token.pickle", "rb") as token:
            creds = pickle.load(token)

    # If no valid credentials, log in
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            try:
                creds.refresh(Request())  # Refresh token
            except Exception as e:
                print(f"Token refresh failed: {e}")
                creds = None  # Force re-authentication if refresh fails
        if not creds:
            # Force re-authentication (browser login)
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        # Save credentials for future use
        with open("token.pickle", "wb") as token:
            pickle.dump(creds, token)

    return build("calendar", "v3", credentials=creds)


def get_event_details():
    """ Gets event name and time using voice commands """
    speak("What is the event?")
    event_name = listen()

    if not event_name:
        speak("Sorry, I couldn't hear the event name. Please try again.")
        return None, None
    print("When should this event take place? For example You can say 'tomorrow at 5 PM' or 'next Monday at 10 AM'.")
    speak("When should this event take place? For example You can say 'tomorrow at 5 PM' or 'next Monday at 10 AM'.")
    spoken_time = listen()

    if not spoken_time:
        speak("Sorry, I couldn't hear the time. Please try again.")
        return None, None

    # Convert spoken time into a date format
    parsed_time = dateparser.parse(spoken_time)

    if parsed_time:
        event_time = parsed_time.strftime("%Y-%m-%dT%H:%M:%S")
        speak(f"Got it! Scheduling '{event_name}' on {parsed_time.strftime('%A, %B %d at %I:%M %p')}.")
        return event_name, event_time
    else:
        speak("Sorry, I couldn't understand the date and time. Please try again.")
        return None, None

from datetime import datetime, timedelta

def add_event_to_calendar(event_name, event_time):
    """ Adds an event to Google Calendar """
    service = authenticate_google()

    try:
        # Convert event_time string to datetime object
        event_time_obj = datetime.strptime(event_time, "%Y-%m-%dT%H:%M:%S")

        # Add 1 hour for event end time
        end_time_obj = event_time_obj + timedelta(hours=1)

        event = {
            "summary": event_name,
            "start": {"dateTime": event_time, "timeZone": "Asia/Kolkata"},
            "end": {"dateTime": end_time_obj.strftime("%Y-%m-%dT%H:%M:%S"), "timeZone": "Asia/Kolkata"},
        }

        event_result = service.events().insert(calendarId="primary", body=event).execute()

        speak(f"Event '{event_name}' has been added to your Google Calendar.")
        print(f"✅ Event added: {event_result.get('htmlLink')}")  # Prints event link

    except Exception as e:
        speak("Sorry, I couldn't add the event due to an error.")
        print(f"Error: {e}")


def search_wikipedia(query):
    """Search Wikipedia via voice and open the page."""
    try:
        speak(f"Searching Wikipedia for {query}...")
        result = wikipedia.summary(query, sentences=2)  # Get a short summary
        speak(result)

        search_url = f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"
        print(f"Opening Wikipedia URL: {search_url}") 

        # Open Wikipedia page in browser
        webbrowser.get().open(search_url)

    except wikipedia.exceptions.DisambiguationError:
        speak("There are multiple results. Please be more specific.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I couldn't find any information on Wikipedia.")

def take_selfie():
    """Capture a selfie and save it."""
    speak("Taking a selfie in 3 seconds. Get ready!")
    
    cam = cv2.VideoCapture(0)  # Open webcam
    cv2.waitKey(3000)  # Wait 3 seconds before capturing

    ret, frame = cam.read()
    if ret:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        filename = f"selfie_{timestamp}.png"
        cv2.imwrite(filename, frame)
        speak("Selfie taken successfully.")
    else:
        speak("Sorry, I couldn't take a selfie.")
    
    cam.release()
    cv2.destroyAllWindows()

def take_note():
    """Take a voice note and save it with a timestamp."""
    speak("What should I write?")
    note = listen()

    if note:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("notes.txt", "a") as file:
            file.write(f"{timestamp} - {note}\n")
        speak("Note saved successfully.")
    else:
        speak("I couldn't hear anything. Please try again.")

def read_notes():
    """Read saved notes from the file."""
    try:
        with open("notes.txt", "r") as file:
            notes = file.readlines()
        if notes:
            speak("Here are your saved notes.")
            for note in notes[-5:]:  # Reads last 5 notes
                speak(note.strip())
        else:
            speak("You have no saved notes.")
    except FileNotFoundError:
        speak("No notes found.")

def delete_notes():
    """Delete all saved notes."""
    with open("notes.txt", "w") as file:
        file.truncate(0)
    speak("All notes have been deleted.")


app_paths = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "vlc": r"C:\\Program Files\\VideoLAN\\VLC\\vlc.exe",
    "word": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\WINWORD.EXE",
    "excel": r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    "powerpoint": r"C:\\Program Files\\Microsoft Office\\root\\Office16\\POWERPNT.EXE",
    "steam": r"C:\\Program Files (x86)\\Steam\\Steam.exe",
    "epic games": r"C:\\Program Files\\Epic Games\\Launcher\\Portal\\Binaries\\Win64\\EpicGamesLauncher.exe"

}

load_dotenv()

# Initialize Speech Engine
engine = pyttsx3.init()

# Initialize Spotify API Authentication
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=os.getenv("SPOTIPY_CLIENT_ID"),
    client_secret=os.getenv("SPOTIPY_CLIENT_SECRET"),
    redirect_uri=os.getenv("SPOTIPY_REDIRECT_URI"),
    scope="user-read-playback-state,user-modify-playback-state"
))

def speak(text):
    """ Convert text to speech """
    engine.say(text)
    engine.runAndWait()


def get_date_time():
    now = datetime.now()
    date = now.strftime("%d %B %Y")  
    time = now.strftime("%I:%M:%S %p") 
    day = now.strftime("%A")  
    return f"{day}, {date} | {time}"
 
def speak(text):
    """ Convert text to speech """
    engine.say(text)
    engine.runAndWait()

def weather_listen():
    """ Listen for a voice command """
    recognizer = sr.Recognizer() 
    with sr.Microphone() as source:
        print("🎙️ Listening for city name...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            city = recognizer.recognize_google(audio, language='en-in')
            print(f"🗣️ You said: {city}")
            return city
        except sr.UnknownValueError:
            return "I couldn't understand the city name."
        except sr.RequestError:
            return "Error with the speech recognition service."

# OpenWeatherMap API Key
WEATHER_API_KEY = "24af3fb524434959043886b890cae7d5" 
def get_weather(city):
    """ Fetch weather details for a given city """
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()

        if response.status_code == 200:
            temperature = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]

            weather_report = (f"The weather in {city} is {description}. "
                              f"The temperature is {temperature}°C with {humidity}% humidity, "
                              f"and the wind speed is {wind_speed} meters per second.")
            return weather_report
        else:
            return f"Check your city name or try again. Error: {data.get('message', 'Unknown error')}"
    
    except requests.exceptions.RequestException as e:
        return "Unable to connect to the weather service. Please check your internet connection."

def play_spotify(song_name):
    """ Search for a song and open it in Spotify """
    results = sp.search(q=song_name, limit=1, type='track')

    if results['tracks']['items']:
        track = results['tracks']['items'][0]
        track_uri = track['uri']
        track_url = track['external_urls']['spotify']

        if os.getenv("SPOTIFY_PREMIUM") == "true":
            try:
                sp.start_playback(uris=[track_uri])
                speak(f"Playing {track['name']} by {track['artists'][0]['name']} on Spotify.")
            except:
                speak("I can't play music directly. Opening it in Spotify instead.")
                webbrowser.open(track_url)
        else:
            speak(f"Opening {track['name']} by {track['artists'][0]['name']} in Spotify.")
            webbrowser.open(track_url)
    else:
        speak("I couldn't find that song on Spotify.")

# Configure Gemini API
API_KEY = "AIzaSyBLF0LzV86rienyeGoQBzHyKN_RhvzEwJk"  
genai.configure(api_key=API_KEY)

recognizer = sr.Recognizer()
engine = pyttsx3.init()
newsapi = "bb666b280d12465db5f39f20b0885529"

def open_app(app_name):
    """ Open an application if found in the dictionary """
    if app_name in app_paths:
        app_path = app_paths[app_name]
        speak(f"Opening {app_name}")
        os.startfile(app_path)  # Open the application
        print(f"Trying to open: {app_paths[app_name]}")

    else:
        speak(f"Sorry, I don't know how to open {app_name}")

def close_app(app_name):
    """Close an application if found in the process list."""
    process_names = {
        "notepad": "notepad.exe",
        "calculator": "calc.exe",
        "vlc": "vlc.exe",
        "word": "WINWORD.EXE",
        "excel": "EXCEL.EXE",
        "powerpoint": "POWERPNT.EXE",
        "steam": "steam.exe",
        "epic games": "EpicGamesLauncher.exe"
    }

    if app_name in process_names:
        process_name = process_names[app_name]
        try:
            subprocess.run(["taskkill", "/F", "/IM", process_name], check=True)
            speak(f"Closing {app_name}")
            print(f"Closed {app_name}")
        except subprocess.CalledProcessError:
            speak(f"Could not close {app_name}. Maybe it's not running.")
            print(f"Failed to close {app_name}")
    else:
        speak(f"Sorry, I don't know how to close {app_name}")

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    """Processes commands using Google Gemini AI."""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash")  # Using Gemini
        response = model.generate_content(command)
        return response.text  # Return AI-generated response
    except Exception as e:
        return f"Error: {str(e)}"

def listen():
    """ Listen for a voice command """
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("🎙️ Listening for a command...")
        recognizer.adjust_for_ambient_noise(source,duration=0.5)
        audio = recognizer.listen(source)
        
        try:
            command = recognizer.recognize_google(audio,language='en-in')
            print(f"🗣️ You said: {command}")
            return command.lower()
        except sr.UnknownValueError:
            print("❌ Could not understand the command.")
            return None
        except sr.RequestError:
            print("❌ Issue with the speech recognition service.")
            return None


def processCommand(c):
    print(f"Processing command: {c}")
    if "open google" in c.lower():
        speak("What should I search on Google?")
        query = listen().lower() 
        webbrowser.open(f"https://www.google.com/search?q={query}")
        speak(f"Searching for {query} on Google")
    elif "open youtube" in c.lower():
        speak("What should I search on Youtube?")
        query = listen().lower()
        webbrowser.open(f"https://www.youtube.com/search?q={query}")
        speak(f"Searching for {query} on Youtube")
    elif "open facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "open instagram" in c.lower():
        webbrowser.open("https://instagram.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://whatsapp.com")
    elif "open hotstar" in c.lower():
        speak("What should I search on JioHotstar?")
        query = listen().lower() 
        webbrowser.open(f"https://www.hotstar.com/in/{query}")
        speak(f"Searching for {query} on JioHotstar")
    elif "tell me a joke" in c.lower():
        joke=pyjokes.get_joke()
        print(joke)
        speak(joke)
    elif "take screenshot" in command or "take a screenshot" in command:
        speak("Please tell me the name of the screenshot file")
        name=listen().lower()
        speak("Hold the screen for few seconds, i am taking the screenshot")
        time.sleep(3)
        img = pyautogui.screenshot()
        img.save(f"{name}.png")
        speak("I am done with the screenshot, the screenshot is saved in main folder")
    elif "play" in command:
        song_name = command.replace("play", "").strip()
        play_spotify(song_name)
    elif "open" in command:
            app_name = command.replace("open", "").strip().lower()
            open_app(app_name)
    elif "close" in command:
        app_name = command.replace("close", "").strip().lower()
        close_app(app_name)
    elif "date" in command or "day" in command or "time" in command:
        print(get_date_time())
        speak(get_date_time())
    elif "weather" in command.lower():
        speak("Which city's weather would you like to check?")
        city_name = weather_listen()

        if city_name:
            weather_info = get_weather(city_name)
            print(weather_info)
            speak(weather_info)
        else:
            speak("I couldn't understand the city name. Please try again.")
    
    elif "take a note" in command:
        take_note()
    elif "read my notes" in command:
        read_notes()
    elif "delete my notes" in command:
        delete_notes()
    elif "take a selfie" in command:
        take_selfie()
    elif "search for" in command:
        query = command.replace("search for", " ").strip()
        search_wikipedia(query)

    elif "add event" in command.lower() or "schedule a event" in command.lower() or "add a event" in command.lower():
        speak("Let's add an event to your Google Calendar.")
        event_name, event_time = get_event_details()
        if event_name and event_time:
            add_event_to_calendar(event_name, event_time)
        else:
            speak("Sorry, I couldn't add the event. Please try again.")
        
    elif "send message" in command or "send a message" in command:
        send_whatsapp_message()

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=us&apiKey={newsapi}")
        if r.status_code == 200:
            data = r.json()
            articles = data.get("articles", [])
        
            for article in articles: 
                print(article['title'])
                speak(article['title'])
    else:
        #Let OpenAI handle the request
        output = aiProcess(c)
        print(output)
        speak(output)
    
   

if __name__ == "__main__":
    speak("Initializing Jarvis.....")

    while True:
        # Listen for the wake word "JARVIS"
        # Obtain audio from the microphone
        r = sr.Recognizer()
        
        # Recognize speech using Google
        print("Recognizing....")

        try:
            with sr.Microphone() as source:
                print("Listening....")
                audio = r.listen(source,timeout=3,phrase_time_limit=2)
            word = r.recognize_google(audio)

            if(word.lower() == "jarvis"):
                from greet import greetMe
                greetMe()
                speak("Please tell me, How can I help you ?")
                #Listen for Command
                with sr.Microphone() as source:
                    print("Jarvis Active....")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    
                    processCommand(command)

        except Exception as e:
            print("Error; {0}".format(e))
