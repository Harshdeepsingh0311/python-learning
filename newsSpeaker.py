# News Speaker

import requests
import json
from win32com.client import Dispatch

def speak(str):
    speaker = Dispatch('SAPI.SpVoice')
    speaker.Voice = speaker.GetVoices().Item(2)
    speaker.Rate = 0.5
    speaker.Speak(str)

if __name__ == '__main__':
    speak('News for today!, Lets begin')
    url = 'https://newsapi.org/v2/top-headlines?sources=the-times-of-india&apiKey=611ae3d09b094d21afbf46708e78c806'
    news = requests.get(url).text
    loaded = json.loads(news)
    arts = loaded['articles']

    for art in arts:
        speak(art['title'])
        speak('Moving to the next news!!')
    speak('Thanks for listening.......')