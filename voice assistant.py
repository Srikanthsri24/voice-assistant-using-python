
import speech_recognition as sr

import datetime as dt

import pyttsx3

 
import wikipedia as wiki


listener = sr.Recognizer()

speaker = pyttsx3.init()

rate = speaker.getProperty('rate')
speaker.setProperty('rate', 250)

def speak(text):
    speaker.say('Yes Boss, ' + text)
    speaker.runAndWait()

speak('tell me boss...')

def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_sphinx(voice)
            command = command.lower()
            if 'siri' in command:
                print(command)
                speak(command)

    except:
        print('check your Microphone')
    return command
while True:
    user_command = take_command()
    if 'close' in user_command:
        print('See you again boss. I will be there when ever you call me...')
        speak('See you again boss. I will be there when ever you call me...')
        break
    elif 'time' in user_command:
        cur_time = dt.datetime.now().strftime("%I:%M %p")
        print(cur_time)
        speak(cur_time)
    elif 'play' in user_command:
        user_command = user_command.replace('play ', '')
        print('playing ' + user_command)
        speak('playing ' + user_command + ', enjoy boss...')
        pk.playonyt(user_command)
        break
    elif 'search for' in user_command or 'google' in user_command:
        user_command = user_command.replace('search for ', '')
        user_command = user_command.replace('google ', '')
        speak('searching for ' + user_command)
        pk.search(user_command)
        