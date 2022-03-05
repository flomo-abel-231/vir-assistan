import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():
    with sr.Microphone() as source:
        print('listening...')
        voice = listener.listen(source)
        command = listener.recognize_google(voice)
        command = command.lower()
        if "Flomo" in command:
            command = command.replace('Flomo ', '')
            print(command)
    return command


def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command: 
        song = command.replace('play', '')
        talk('playing ' + song)
        pywhatkit.playonyt(song)

    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk('Current time is ' + time)

    elif 'who is' in command:
        person = command.replace('who is', '')
        info = wikipedia.summary(person, 1) 
        print(info)
        talk(info)

    elif 'stupid' in command:
        talk(" Flomo,  cannot respond to that.")

    elif 'f***' in command:
        talk(" Flomo, cannot respond to that.  ")

    elif 'are you single' in command:
        talk(' I am a machine.')

    elif 'joke' in command:
        talk(pyjokes.get_joke())

    elif 'thank you ' or 'thanks'  in command:
        talk('You are absolutely welcome')

    else:
        talk('Flomo, Please say the command again.')


while True:
    run_alexa()