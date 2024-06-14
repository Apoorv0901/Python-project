import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voice = engine.getProperty('voices')

engine.setProperty('voice',voice[1].id)
engine.setProperty('rate',130)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning")
    elif hour >= 12 and hour < 18:
        speak("Good aftet noon")
    else :
        speak("Good Evening")

    speak("I am Nova , please tell me How can i help you")

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.energy_threshold = 10000
        r.adjust_for_ambient_noise(source,1.2)
        print("Listening.....")
        r.pause_threshold = 2
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query = r.recognize_google(audio,language = "en-in")
        print(f"User said : {query}\n")

    except Exception as e :
        print('Say that again please')
        return 'None'
    return query

if __name__ == "__main__":
    wishMe()
    while True :
        query = takeCommand().lower()

        #logic to execute cammands
        if 'wikipedia' in query :
            speak("searching wikipedia.....")
            query = query.replace("wikipedia","")
            result = wikipedia.summary(query,sentences = 2)
            speak('According to Wikipedia')
            print(result)
            speak(result)
        elif 'open youtube' in query:
            webbrowser.open('youtube.com')
        elif 'open google' in query:
            webbrowser.open('goggle.com')
        elif 'play music' in query:
            music_dir = "C:\music\playlist"
            songs = os.listdir(music_dir)
            print(songs)
            ox.startfile(os.path.join(music_dir,songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}");
        elif 'open code' in query:
            codepath = "C:\\Users\\DELL\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)