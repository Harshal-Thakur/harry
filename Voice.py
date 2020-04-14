import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
from googletrans import Translator
import webbrowser
import os
import smtplib
import cv2

engine = pyttsx3.init("sapi5")
voices = engine.getProperty("voices")
#print(voices)
engine.setProperty("voice",voices[0].id)


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
        
    speak("This is Harshal's personal voice assistant Harry. how may I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
    
    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said: ",{query},"\n")
    except Exception as e:
        print(e)
        print("Say that again please...")
        return "None"
    
    return query


def sendEmail(to,content):
    server = smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()   #identify yourself to the server
    server.starttls()
    server.login(os.environ["MY_EMAIL_ID"],os.environ["MY_EMAIL_PWD"])
    server.sendmail(os.environ["MY_EMAIL_ID"],to,content)
    server.close()


if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()
        
        if "wikipedia" in query:
            speak("Searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences=2)
            print(results)

            translator = Translator()
            hindi = translator.translate(results, dest='hi')
            hindi = hindi.text
            print("\n",hindi)
            
            speak("According to wikipedia")
            speak(results)
            #speak(hindi)
            
        elif "open google" in query:
            print("Opening Google...")
            speak("Opening Google...")
            webbrowser.open("google.com")
            
        elif "open youtube" in query:
            print("Opening Youtube...")
            speak("Opening Youtube...")
            webbrowser.open("youtube.com")
        
        elif "open facebook" in query:
            print("Opening Facebook...")
            speak("Opening Facebook...")
            webbrowser.open("facebook.com")
            
#        elif "play music" in query:
#            music_dir = "path"
#            songs = os.listdir(music_dir)
#            print(songs)
#            os.startfile(os.path.join(music_dir , songs[0]))
            
        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Sir, the time is ",strTime)
            speak("Sir, the time is")
            speak(strTime)
            
        elif "open car game" in query:
            gamePath = "C:\Program Files (x86)\HighwayPursuit\HighwayPursuit.exe"
            print("Opening Car Game...")
            speak("opening Car Game")
            os.startfile(gamePath)
        
        elif "send email to harshal" in query:
            try:
                speak("What is the message that you want to send?")
                content = takeCommand()
                to = "harshalthakur010@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully sent to harshal!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please Check your Internet Connection or provide proper Email ID and password")
                
        elif "send email to sarvesh" in query:
            try:
                speak("What is the message that you want to send?")
                content = takeCommand()
                to = "sarvesh3343t@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully sent to sarvesh!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please Check your Internet Connection or provide proper Email ID and password")
                
        elif "send email to dad" in query:
            try:
                speak("What is the message that you want to send?")
                content = takeCommand()
                to = "daduthakur1234@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully sent to dad!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please Check your Internet Connection or provide proper Email ID and password")
                
        elif "send email to anuradha" in query:
            try:
                speak("What is the messsage that you want to send?")
                content = takeCommand()
                to = "imanuradha.ac@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully to Anuradha!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please check your Internet Connection or provide proper Email ID and password")
                
        elif "send email to satya ma'am" in query:
            try:
                speak("What is the messsage that you want to send?")
                content = takeCommand()
                to = "satyawanigounder@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully to Satya mam!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please check your Internet Connection or provide proper Email ID and password")
                
        elif "send email to yash" in query:
            try:
                speak("What is the messsage that you want to send?")
                content = takeCommand()
                to = "yashtupkari@yahoo.com"
                sendEmail(to,content)
                speak("Email has been successfully to Yash!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please check your Internet Connection or provide proper Email ID and password")
                
        elif "send email to pradeep" in query:
            try:
                speak("What is the message that you want to send?")
                content = takeCommand()
                to = "prdp.patil@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully sent to Pradeep!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please check your Internet Connection or provide proper Email ID and password")
          
        elif "send email to Hitesh" in query:
            try:
                speak("What is the message that you want to send?")
                content = takeCommand()
                to = "hiteshshirsat21@gmail.com"
                sendEmail(to,content)
                speak("Email has been successfully sent to Hitesh!")
            except Exception as e:
                print(e)
                speak("Sorry! Your Email is not sent. Please check your Internet Connection or provide proper Email ID and password")
            
        elif "open camera" in query:
            print("Opening Camera...")
            print("Press Q to QUIT")
            speak("Opening Camera...")
            speak("Press Q to QUIT")
            
            a = cv2.VideoCapture(0)
            
            while True:
                active,frame = a.read()
                cv2.imshow("Harry's Camera",frame)
                
                k = cv2.waitKey(1)
                
                if(k==ord("q") or k==ord("Q")):
                    break
            
            cv2.destroyAllWindows()
            a.release()
            
        elif "growing tornado" in query:
            print("Showing a Growing Tornado...")
            speak("Showing a Growing Tornado...")
            import Animated_plot
        
        elif "bye" in query:
            speak("Bye!")
            exit()
        
        speak("Thank You!")
        break

