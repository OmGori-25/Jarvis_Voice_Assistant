import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import pyaudio
import webbrowser
import os
import smtplib
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
# print(voices)
engine.setProperty('voice',voices[0].id)
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12 :
        speak("Good Morning!")
    elif hour>=12 and hour<=18:
        speak("Good Afternoon!")
    elif hour>18 and hour<=20 :
        speak("Good Evening!")
    else :
        speak("Goodnight!")
    speak("I am Jarvis , Sir or Madame . Please tell me how may I help you")

def takeCommand():
    """It takes microphone input from the user and returns the output in the form of string"""
    r=sr.Recognizer()
    with sr.Microphone() as source :
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)

    try:
        print("Recognizing...")
        query=r.recognize_google(audio,language='en-in')
        print(f"User said :{query}\n")
    except Exception as e :
        print("Say that again please :")
        return "None"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('om.gori16196@sakec.ac.in','password')
    server.sendmail('om.gori16196@gmail.com',to,content)
    server.close()

if __name__=="__main__":
    wishMe()
    while True :
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")
        elif 'open google' in query:
            webbrowser.open("google.com")
        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play music' in query :
            music_dir='C:\\Users\\OM\\Music'
            songs=os.listdir(music_dir)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif 'the time' in query :
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The time is {strTime}")
        elif 'open code' in query :
            codepath="C:\\Users\\OM\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
        elif 'email to omkar' in query:
            try:
                speak("What should I send?")
                content=takeCommand()
                to="omsgori@gmail.com"
                sendEmail(to,content)
                speak("Email is sent")
            except Exception as e :
                print(e)
                speak("Sorry Sir , I am not able to send the email Please try again")

        elif 'quit' in query:
            exit()
    #Logic for executing task based on query
