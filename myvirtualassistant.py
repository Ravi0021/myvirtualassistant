import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour  = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<16:
        speak("Good Afternoon!")

    elif hour>=16 and hour<20:
        speak("Good Evening!")

    elif hour>=20 and hour<0:
        speak("Good Night!")

    speak("I am Ehsaas & Sir How may i help you")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f'User Said: {query}\n')

    except Exceptionas as e:
        print("Say that again please")
        return "None"
    return query


if __name__ == '__main__':
    wishMe()
    while True:
        query = takeCommand().lower()

        if 'wikipedia' in query:
            speak('searching Wikipedia...')
            query = query.replace('wkipedia', "")
            results = wikipedia.summary(query, sentences=2)
            speak("according to Wikipedia")
            print(results)
            speak(results)

        elif 'open google' in query:
            webbrowser.open('google.com')

        elif 'open youtube' in query:
            webbrowser.open('youtube.com')

        elif 'the time' in query:
            strTime = datetime.datetime.now().strTime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")