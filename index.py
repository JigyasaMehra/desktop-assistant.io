print("hello")
import webbrowser


import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import pyjokes
import pyautogui

listener = sr.Recognizer()
engine = pyttsx3.init()

def wishme():
    hour = datetime.datetime.now().hour
    if hour>=0 and hour<=12:
        engine.say('Good Morning Boss!  I am your Loki. What can I do to please you?')
        engine.runAndWait()
    elif hour>12 and hour<18:
        engine.say('Good Afternoon Boss!  I am your Loki. What can I do to help you?')
        engine.runAndWait()
    else:
        engine.say('good evening boss!  I am your Loki. What can I do for you?')
        engine.runAndWait()

wishme()
def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('listening..')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'loki' in command:
                command = command.replace('loki','')
                print(command)

    except:
        pass
    return command
def run_loki():
  
         command = take_command()
         print(command)
         command = take_command()
         print(command)
         if 'play' in command:
             song = command.replace('play','')
             talk('playing' + song )
             pywhatkit.playonyt(song)
         elif 'time' in command:
             time = datetime.datetime.now().strftime('%I:%M %p')
             talk('Current time is ' + time)
         elif 'wikipedia' in command:
            person = command.replace('search','')
            info = wikipedia.summary(person, 1)
            print(info)
            talk(info)
         elif 'do you love me' in command:
             talk('Miss! I love you 3000. I hope you love me too')
         elif 'I love you' in command:
             talk('I love you more maam')
         elif 'girlfriend' in command:
             talk('No No! I dont have any. I love Jigyasa Maam, but she is dating someone else. ohh no I feel jealous.')
         elif 'boyfriend' in command:
             talk('Sorry!, Its a secret..')
         elif 'your name' in command:
             talk('My name is Loki.')
         elif 'introduce' in command:
             talk('Hello everyone! Myself Loki. I am Odin Son. I am from Asgard. Currently I am living here to help you. Tell me how can I make your life easy?')
         elif 'vaibhav' in command:
             talk('Hello Vaibhav Sir!! I am so glad to meet you sir.  Jigyasa maam made me to help you and to entertain you. So, tell me sir, how can I help you?')
         elif 'how are you' in command:
             talk('I am fantastic maam')
         elif 'joke' in command:
             talk(pyjokes.get_joke())
         elif 'open google' in command:
             webbrowser.open('www.google.com')
         elif 'youtube' in command:
             webbrowser.open('http://www.youtube.com')
         elif 'open instagram' in command:
             webbrowser.open('www.instagram.com')
         elif 'open email' in command:
             webbrowser.open('https://mail.google.com/mail/u/0/#inbox')
         elif 'open telegram' in command:
             webbrowser.open('https://web.telegram.org/z/')
         elif 'search' in command:
             search = 'http://www.google.com/search?q='+command
             webbrowser.open(search)
         elif 'start movie' in command:
             mov = command.replace('start movie','')
             movie = 'https://myflixer.pw/search/'+mov
             webbrowser.open(movie)
     
         elif 'volume up' in command:
             pyautogui.press('volumeup')
         elif 'volume down' in command:
             pyautogui.press('volumedown')
         elif 'volume mute' in command:
             pyautogui.press('volumemute')
         
     
     
         else:
             talk('sorry boss! I cannt understand what you are saying, please say it clearly')

while True: 
    run_loki()
           
     