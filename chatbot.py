from chatterbot import ChatBot #import the chatbot
from chatterbot.trainers import ChatterBotCorpusTrainer
import os
import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice",voices[1].id)

bot = ChatBot('Bot')
trainer = ChatterBotCorpusTrainer(bot)

corpus_path = r'C:\Users\HARSHAL\Anaconda3\Lib\site-packages\chatterbot_corpus\data\english\\'

for file in os.listdir(corpus_path):
    trainer.train(corpus_path + file)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
    
def wishMe():
    hour = int(datetime.datetime.now().hour)
    
    if hour>=0 and hour<12:
        speak("Good morning Sir!") 
    elif hour>=12 and hour<18:
        speak("Good Afternoon Sir!")     
    else:
        speak("Good Evening Sir!")
        
    speak("This is Harshal's personal voice assistant. how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query


if __name__ == "__main__":
    wishMe()
    
    while True:
        message = takeCommand().lower()
        print("You: ", message)
        if message.strip() == 'bye':
            speak('Bye')
            print('ChatBot: Bye')
            break
        else:
            reply = bot.get_response(message)
            speak(reply)
            print('ChatBot: ', reply)
