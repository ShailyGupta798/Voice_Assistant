# First download pyaudio, speech recognition or pyspeech  and gtts packages.
"""PyAudio provides Python bindings for PortAudio, the cross-platform audio I/O library.
 With PyAudio, you can easily use Python to play and record audio.
 gTTS (Google Text-to-Speech), a Python library and CLI tool to interface with Google Translate's text-to-speech API.
 smtplib library to send email"""
 
import speech_recognition as sr
from gtts import gTTS
import os
from time import ctime
import datetime
import wikipedia
import webbrowser

# mpg321  is  a  free  command-line  mp3  player, which uses the mad audio decoding library.
def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='en')
    tts.save("audio.mp3")
    os.system("mpg321 audio.mp3")

def recordAudio():
    # Auto recorded audio
   r = sr.Recognizer()
   how = sr.AudioFile('time.wav')
   with how as source:
       audio = r.record(source)
       
   """
   record audio with microphone
   sr.Microphone.list_microphone_names()
   with sr.Microphone(device_index) as source:
    print("Say something!")
    audio = r.listen(source)"""
     
    # Speech recognition using Google Speech Recognition
   data = ""
   try:
        # Uses the default API key
        # To use another API key: `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
        
        data = r.recognize_google(audio)
        speak("You said:"+data)
        
   except sr.UnknownValueError:
        speak("Google Speech Recognition could not understand audio")
   except sr.RequestError as e:
        speak("Could not request results from Google Speech Recognition service; {0}".format(e))
    
   return data

def jarvis(data):
    if "how are you" in data:
        speak("I am fine")
        data = recordAudio()

    elif "what time is it" in data:
        speak("The time is: "+ ctime())

    elif "where is" in data:
        data = data.split(" ")
        location = data[2]
        speak("Hold on Shaily, I will show you where " + location + " is.")
        os.system("firefox https://www.google.com/maps/place/" + location + "/")
    
    elif "wikipedia" in data:
        data=data.replace("wikipedia","")
        results=wikipedia.summary(data,sentences=2)
        print(results)
        speak(results)
        
    elif   'open youtube' in data:
        webbrowser.open("youtube.com")
        
    elif 'open google' in data:
        webbrowser.open("google.com")
        
    
        
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour <12:
        speak("Good Morning!")
        
    elif hour>=12 and hour<18:
        speak("good Afternoon!")
    else:
        speak("good Evening!")

# initialization
wishMe()
speak("Hi Shaily, what can I do for you?")
data = recordAudio()
data="wikipedia sharukh khan"
jarvis(data)
