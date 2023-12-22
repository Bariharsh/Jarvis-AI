import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib

engine = pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishme():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour <12:
        speak("Good morning Boss!,Hello Boss i am friday,how may i help you")
    elif hour>=12 and hour<18:
        speak("Good Afternoon Boss!,Hello Boss i am friday,how may i help you")
    else:
        speak("Good Evening Boss!,Hello Boss i am friday,how may i help you")


def takeCommand():
    r =sr.Recognizer()
    with sr.Microphone() as source:
        print("listening.....")
        r.pause_threshold=1
        r.energy_threshold=100
        audio=r.listen(source)

    try:
        print("Recognizing....")
        query=r.recognize_google(audio,language="en-in")
        print(f"user siad:{query}\n")

    except Exception as e:
        speak("say that agian please...")
        return "none"
    return query

def sendEmail(to,content):
    server=smtplib.SMTP("smtp.gmail.com",587)
    server.ehlo()
    server.starttls()
    server.login("youremail@gmal.com","your-password")
    server.sendmail("youremail@gmal.com",to,content)
    server.close()

if __name__ == '__main__':
    wishme()
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("seaching wikipedia....")
            query=query.replace("wikipedia","")
            results=wikipedia.summary(query,sentence=2)
            speak("acording to wikipedia")
            speak(results)
        elif "open youtube" in query:
            webbrowser.open("youtube.com")

        elif "open google" in query:
            webbrowser.open("google.com")

        elif "open stackoverflow" in query:
            webbrowser.open("stackoverflow.com")

        elif "play music" in query:
            music_dir="c:\\"
            songs=os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir,songs[0]))

        elif "the time" in query:
            strTime=datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir,the time is {strTime}")

        elif "open code" in query:
            codepath="C:\\softwares\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif "email to harsh" in query:
            try:
                speak("what should i say?")
                content=takeCommand()
                to ="harshbari227@gmail.com"
                sendEmail(to,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry boss i am not able to send this email")
