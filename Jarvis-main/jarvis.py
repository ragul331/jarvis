import pyttsx3  #py -m pip install pyttsx3
import datetime
import speech_recognition as sr #py -m pip install SpeechRecognition
import wikipedia #py -m pip install wikipedia
import smtplib
import webbrowser as wb
import os
import pyautogui #py -m pip install pyautogui
import psutil #py -m pip install psutil
import pyjokes #py -m pip install pyjokes
import pyaudio #python -m pip install pyaudio

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voices', voices[0].id)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def time():
    Time=datetime.datetime.now().strftime("%I:%M:%S")
    speak("The current time is")
    speak(Time)

def date():
    year=int(datetime.datetime.now().year)
    month=int(datetime.datetime.now().month)
    date=int(datetime.datetime.now().day)
    speak("The current date is")
    speak(date)
    speak(month)
    speak(year)

def wishme():
    speak("Welcome back sir!")
    time()
    date()
    hour = datetime.datetime.now().hour
    if hour >= 6 and hour<12:
        speak("Good Morning Sir!")
    elif hour >=12 and hour<16:
        speak("Good afternoon sir!")
    elif hour >=16 and hour<20:
        speak("Good evening sir!")
    else:
        speak("Good night sir!")
    speak("Jarvis at your service. Please tell me how can i help you?")
   
def takeCommand():
    r= sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold=1
        audio=r.listen(source)
    try:
        print("Recongnizing...")
        query =r.recognize_google(audio, language='en-in')
        print(query)

    except Exception as e:
        print(e)
        speak("Say that again please...")
        return None

    return query

def sendemail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.eclo()
    server.strattls()
    server.login("pradhiveragul@gmail.com","VVVVV")
    server.sendmail("pradhiveragul@gmail.com",to,content)
    server.close()

def screenshot():
    img=pyautogui.screenshot()
    img.save("D:\STUDY Material\My_Projects\ss.png")

def cpu():
    usage = str(psutil.cpu_percent())
    speak("CPU is at"+usage)
    battery=psutil.sensors_battery()
    speak("Battery is at")
    speak(battery.percent)

def joke():
    speak(pyjokes.get_joke())

if __name__ =="__main__":
    wishme()
    while True:
        query=takeCommand().lower()

        if "time" in query:
            time()

        elif "date" in query:
            date()
       
        elif "wikipedia" in query:
            speak("searching...")
            query=query.replace("wikipedia","")
            result=wikipedia.summary(query,sentences=2)
            print(result)
            speak(result)
       
        elif "send email" in query:
            try:
                speak("What should I say?")
                content = takeCommand()
                to="xyz@gmail.com"
                sendemail(to,content)
                speak("Email has been sent!")
            except Exception as e:
                print(e)
                speak("Unable to send the email")
       
        elif "search in chrome" in query:
            speak("what should i search ?")
            chromepath = "C:/Program Files/Google/Chrome/Application/chrome.exe %s"
            search=takeCommand().lower()
            wb.get(chromepath).open_new_tab(search + ".com")
       
        elif "logout" in query:
            os.system("shutdown -1")
       
        elif "shutdown" in query:
            os.system("shutdown /s /t 1")
       
        elif "restart" in query:
            os.system("shutdown /r /t 1")

        elif "play a song" in query:
            songs_dir = "D:\MUSIC"
            songs = os.listdir(songs_dir)
            os.startfile(os.path.join(songs_dir,songs[0]))

        elif "remember that" in query:
            speak("What should I remember?")
            data = takeCommand()
            speak("you said me to remember that "+data)
            remember = open("data.txt",'w')
            remember.write(data)
            remember.close()
       
        elif "do you know anything" in query:
            remember=open("data.txt",'r')
            speak("you said me to remember that "+remember.read())

        elif "screenshot" in query:
            screenshot()
            speak("Done!")

        elif "cpu" in query:
            cpu()

        elif "joke" in query:
            joke()

        elif "offline" in query:
            quit()