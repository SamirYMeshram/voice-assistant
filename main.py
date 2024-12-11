import speech_recognition as sr
import pyttsx3
import requests
import json
import time
from datetime import datetime
import webbrowser
import os
import pyautogui
import wikipedia
import calendar
from apscheduler.schedulers.background import BackgroundScheduler  # For task scheduling
import pygame
import logging

# Initialize the speech engine
engine = pyttsx3.init()

# Set voice properties (optional)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Female voice (can be adjusted)

# JSON file to store assistant data
data_file = 'assistant_data.json'

# Set up logging
logging.basicConfig(filename='assistant_log.log', level=logging.DEBUG, format='%(asctime)s - %(message)s')


# Function to load data from JSON file
def load_data():
    try:
        with open(data_file, 'r') as file:
            data = json.load(file)
    except FileNotFoundError:
        data = {}
    return data


# Function to save data to JSON file
def save_data(data):
    with open(data_file, 'w') as file:
        json.dump(data, file, indent=4)


# Function to speak out a text
def speak(text):
    engine.say(text)
    engine.runAndWait()


# Function to listen to user's voice and recognize the speech
def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            print("Recognizing...")
            query = recognizer.recognize_google(audio)
            print("You said: " + query)
            return query
        except sr.UnknownValueError:
            print("Sorry, I could not understand. Please try again.")
            speak("Sorry, I could not understand that.")
            return None
        except sr.RequestError:
            print("Sorry, I'm having trouble with the speech service. Try again later.")
            speak("Sorry, I'm having trouble with the speech service.")
            return None
        except KeyboardInterrupt:
            print("Listening was interrupted. Exiting.")
            return None


# Function to process the speech query and provide an appropriate response
def handle_query(query):
    query = query.lower()

    data = load_data()  # Load current assistant data

    if "joe" in query:
        speak("Hello, I am Joe, your AI assistant. How can I assist you?")
    elif "hello" in query:
        speak("Hello! How can I assist you today?")
    elif "how are you" in query:
        speak("I'm doing great, thank you for asking!")
    elif "your name" in query:
        speak("I am Joe, your AI assistant, ready to help you.")
    elif "time" in query:
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        speak(f"The current time is {current_time}.")
    elif "weather" in query:
        city = query.split("in")[-1].strip()  # Extract city from the query
        weather_report(city)
    elif "search" in query:
        search_term = query.replace("search", "").strip()
        speak(f"Searching for {search_term} on Google.")
        webbrowser.open(f"https://www.google.com/search?q={search_term}")
    elif "open" in query:
        app = query.split("open")[-1].strip()
        open_application(app)
    elif "take screenshot" in query:
        speak("Taking a screenshot.")
        pyautogui.screenshot().save("screenshot.png")
    elif "set reminder" in query:
        reminder_time = query.split("at")[-1].strip()
        set_reminder(reminder_time, data)
    elif "note" in query:
        note = query.replace("note", "").strip()
        take_note(note, data)
    elif "play music" in query:
        play_music(query)  # Passing the query to check if it contains music name
    elif "stop music" in query:
        stop_music()
    elif "open website" in query:
        website = query.replace("open website", "").strip()
        open_website(website)
    elif "goodbye" in query or "exit" in query:
        speak("Goodbye, have a nice day!")
        return False  # Exit the loop
    elif "explain" in query:
        explain_with_gemini(query)  # Use Gemini AI for explanations
    elif "summarize" in query:
        summarize_with_gemini(query)  # Use Gemini AI to summarize text
    elif "run task" in query:
        run_task_with_gemini(query)  # Use Gemini AI to handle complex tasks
    elif "wikipedia" in query:
        query_term = query.replace("wikipedia", "").strip()
        get_wikipedia_info(query_term)
    elif "schedule" in query:  # New functionality: scheduling tasks
        schedule_task(query, data)
    elif "news" in query:  # New functionality: Get latest news
        get_news(query)
    else:
        speak("Sorry, I couldn't understand that. Can you please rephrase?")

    # Save the updated data back to the JSON file
    save_data(data)
    return True


# Weather Report function (using OpenWeatherMap API)
def weather_report(city):
    # Default city in case of invalid input
    if not city or city.lower() == "none":
        city = "Nagpur"

    api_key = "30816f4fea5fd2bd505c7c6b5562e6cd"  # Get an API key from OpenWeatherMap
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&appid={api_key}&units=metric"
    response = requests.get(complete_url)
    try:
        data = response.json()
        if data["cod"] != "404":
            main = data["main"]
            weather = data["weather"][0]
            temperature = main["temp"]
            description = weather["description"]
            speak(f"The temperature in {city} is {temperature}°C with {description}.")
        else:
            speak("City not found. Please make sure the city name is correct.")
            speak("You can try another city or check the spelling.")
    except KeyError:
        speak("Sorry, there was an error fetching the weather data.")
    except Exception as e:
        speak(f"An error occurred: {e}")


# Open application (Chrome, Notepad, etc.)
def open_application(app):
    if "chrome" in app:
        speak("Opening Google Chrome.")
        os.system("start chrome")  # Windows command
    elif "notepad" in app:
        speak("Opening Notepad.")
        os.system("start notepad")
    elif "calculator" in app:
        speak("Opening Calculator.")
        os.system("start calc")
    else:
        speak("Sorry, I can't open that application.")


# Reminder functionality (set a simple reminder)
def set_reminder(reminder_time, data):
    speak(f"Reminder set for {reminder_time}.")
    if "reminders" not in data:
        data["reminders"] = []
    data["reminders"].append(reminder_time)


# Take a note and store it in the JSON data
def take_note(note, data):
    if "notes" not in data:
        data["notes"] = []
    data["notes"].append(note)
    speak(f"Note taken: {note}")


# Wikipedia Information Function
def get_wikipedia_info(query_term):
    try:
        info = wikipedia.summary(query_term, sentences=2)  # Get a short summary
        speak(info)
    except wikipedia.exceptions.DisambiguationError as e:
        speak("There are multiple results for your query. Please be more specific.")
    except wikipedia.exceptions.HTTPTimeoutError:
        speak("There was a timeout error while fetching information.")
    except wikipedia.exceptions.PageError:
        speak("Sorry, I could not find any information on that topic.")
    except Exception as e:
        speak(f"An error occurred: {e}")


# Function to handle chatting with Gemini AI using a POST request
def handle_gemini_request(query):
    speak("Let me think about it.")
    api_key = "AIzaSyCQZzOBPLIffz2kjD_aGInNPJRHYjk5bNw"  # Your Gemini API key
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash-latest:generateContent?key=" + api_key
    headers = {"Content-Type": "application/json"}
    data = {
        "contents": [
            {
                "parts": [
                    {
                        "text": query
                    }
                ]
            }
        ]
    }

    try:
        response = requests.post(url, json=data, headers=headers)
        response.raise_for_status()  # Raise an error for bad responses
        result = response.json()
        if 'content' in result:
            conversation = result['content']
            speak(conversation)
        else:
            speak("Sorry, I couldn't understand your question.")
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        speak("There was an issue connecting to Gemini AI.")


# Function to play music (using Pygame for local music or Webbrowser for YouTube)
def play_music(query):
    speak("Searching for music.")
    music_file = f"{query}.mp3"  # Check for the music with name given by user
    music_path = f"music/{music_file}"  # Local folder where music is stored

    if os.path.exists(music_path):
        speak(f"Playing {query} from local storage.")
        pygame.mixer.init()
        pygame.mixer.music.load(music_path)
        pygame.mixer.music.play()
    else:
        speak(f"{query} not found in local storage. Searching on YouTube.")
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")


# Function to stop music
def stop_music():
    pygame.mixer.music.stop()
    speak("Music stopped.")


# Function for scheduling tasks (new functionality)
def schedule_task(query, data):
    task_details = query.replace("schedule", "").strip()
    speak(f"Scheduling task: {task_details}")
    if "tasks" not in data:
        data["tasks"] = []
    data["tasks"].append(task_details)
    speak(f"Task scheduled: {task_details}")


# Get the latest news (new functionality)
def get_news(query):
    speak("Fetching the latest news.")
    webbrowser.open("https://www.bbc.com/news")


# Main loop to interact with the user continuously
def main():
    speak("Hello, I am Joe. How can I assist you?")
    while True:
        query = listen()
        if query is None:
            time.sleep(5)  # Sleep if no input for 5 seconds
            continue  # Continue listening if no input
        elif not handle_query(query):  # Handle query and stop loop if "exit" or "goodbye"
            break


if __name__ == "__main__":
    main()
