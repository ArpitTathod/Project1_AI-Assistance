
from multiprocessing.spawn import import_main_path
import pyttsx3
import speech_recognition as sr
import webbrowser
import datetime
import wikipedia
import os
import smtplib


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[1].id) 
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio) 
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)   
    if hour>=0 and hour<12:
        speak("Good Morning!") 
    
    elif hour>=12 and hour<18:
        speak("Good Afternoon!")
        
    else:
        speak("Good Evening!")
        
    speak(" I am jarvis Sir. Please tell me how may i help you")    
        
def takeCommand():  
    # It takes microphomne input from the user and return string output
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...") 
        query = r.recongnize_google(audio, Language='en-in')
        print(f"User said: {query}\n")
    
    except Exception as e:
       # print(e) 
        print("Say that again please....")
        return "None"
    return query     


def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('adtathod7@gmai.com', 'TaThod16-here')
    server.sendmail('youremail@gmail.com', to, content)
    server.close()
    
if __name__== "__main__":
      while True:
        # if 1:
        query = takeCommand().lower() #Converting user query into lower case

        # Logic for executing tasks based on query
        if 'wikipedia' in query:  #if wikipedia found in the query then this block will be executed
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2) 
            speak("According to Wikipedia")
            print(results)
            speak(results)
        
        
        elif 'open youtube' in query:
                webbrowser.open("youtube.com")
                
        elif 'open google' in query:
            webbrowser.open("google.com")
            
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")    
        
        elif 'play music' in query:
            music_dir = 'D:\\Python practice\\Project   AI Jarvis songs Nachi Nachi.mp3'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))    
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open code' in query:
            codePath = "D:\\Python Installtion\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)
    
    
        elif 'email to harry' in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to = "arpit16tathod@gmail.com"    
                sendEmail(to, content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Sorry my friend harry bhai. I am not able to send this email")                    
        
    
               
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
                    