import pyttsx3 as pt
from datetime import datetime
import speech_recognition as sr
import wikipedia as wk
import webbrowser as wb
from random import randint
import os
import smtplib

engine = pt.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[2].id)  #Optional


def speak(audio):
    """
    :param audio: to speak
    :return: speaks the param audio
    """
    engine.say(audio)
    engine.runAndWait()


def take():
    global query
    """
    :param: there is no parameter but it takes users voice as input
    :return: returns query in which users string is stored
    """
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print('Listening.....')
        speak('Listening.....')
        r.energy_threshold = 250
        r.pause_threshold = 1
        audio = r.listen(source=source)

    try:
        print("Recognising.....")
        speak("Recognising.....")
        query = r.recognize_google(audio, language='en-in')
        print(f'User: {query}')
        speak(f'User: {query}')

    except Exception as e:
        print(e)
        speak("Say that again please!!")
        return "None"


def wishMe():
    """
    Calculates time through date time module
    :return: greets the user and introduces it
    """
    time = int(datetime.now().hour)
    if time >= 0 and time <= 12:
        print('Good Morning!')
        speak('Good Morning!')
    elif time >= 12 and time <= 18:
        print("Good Afternoon!")
        speak("Good Afternoon!")
    else:
        print('Good Evening!')
        speak('Good Evening!')
    print('I am jarvis, please tell me how may i help you?')
    speak('I am jarvis, please tell me how may i help you?')


def sendMail(content, to):
    """
    :param content: content of the mail
    :param to: email of the person to which email has to be sent
    :return: sends the mail to the person
    """
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('YOUR_MAIL','YOUR_PASSWORD')
    server.sendmail('YOUR_EMAIL', to, content)


if __name__ == '__main__':
    wishMe()
    while True:
        query = take().lower()

        if "wikipedia" in query:
            print('Searching Wikipedia...')
            speak('Searching Wikipedia...')
            query.replace("wikipedia", "")
            results = wk.summary(query, sentences=1)
            print(f'According to wikipedia {results}')
            speak(f'According to wikipedia {results}')

        elif "open youtube" in query:
            wb.open('www.youtube.com')

        elif "open google" in query:
            wb.open('www.google.com')

        elif "open stackoverflow" in query:
            wb.open('www.stackoverflow.com')

        elif "open code" in query:
            code_path = r"YOUR VSCODE DIR"
            os.startfile(code_path)

        elif "play music" in query:
            music = 'YOUR_MUSIC_DIR'
            songs = os.listdir(music)
            randomMusic = randint(0, len(songs)-1)
            os.startfile(os.path.join(music, songs[randomMusic]))

        elif "time" in query:
            strTime = datetime.now().strftime('%H:%M:%S')
            print(f'The time is {strTime}')
            speak(f'The time is {strTime}')

        elif "email" in query:
            try:
                print('What should i send?')
                speak('What should i send?')
                content = take()
                to = 'RECIEVERS_EMAIL'
                sendMail(content, to)
                speak('Email has been sent.')

            except:
                speak('Sorry i am not able to send this email.')
