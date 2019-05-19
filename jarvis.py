import pyttsx3
import webbrowser
import smtplib
import random
import speech_recognition as sr
import wikipedia
import datetime
import wolframalpha
import os
import sys
import json
import requests



engine = pyttsx3.init('sapi5')

client = wolframalpha.Client('Your_App_ID')

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[len(voices)-1].id)

def speak(audio):
    print('Jarvis: ' + audio)
    engine.say(audio)
    engine.runAndWait()

def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning Aiden!')

    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon Aiden!')

    if currentH >= 18 and currentH !=0:
        speak('Good Evening Aiden!')

greetMe()

speak('Hello Aiden, I am your digital assistant LARVIS the Lady Jarvis!')
speak('How may I help you Aiden?')


def myCommand():
   
    r = sr.Recognizer()                                                                                   
    with sr.Microphone() as source:                                                                       
        print("Listening...")
        r.pause_threshold =  1
        audio = r.listen(source)
    try:
        query = r.recognize_google(audio, language='en-in')
        print('User: ' + query + '\n')
        
    except sr.UnknownValueError:
        speak('Sorry Aiden! I didnt get that! Try typing the command!')
        query = str(input('Command: '))

    return query
        

if __name__ == '__main__':

    while True:
    
        query = myCommand()
        query = query.lower()
        
        if "open youtube" in query:
            speak('yes sir')
            webbrowser.open('www.youtube.com')

        elif 'open google' in query:
            speak('yes sir')
            webbrowser.open('www.google.co.in')

        elif 'open gmail' in query:
            speak('yes sir')
            webbrowser.open('www.gmail.com')

        elif "what\'s up" in query or 'how are you' in query:
            stMsgs = ['Just doing my thing!', 'I am fine!', 'Nice!', 'I am nice and full of energy']
            speak(random.choice(stMsgs))

        elif 'email' in query:
            speak('Who is the recipient? ')
            recipient = myCommand()

            if 'me' in recipient:
                try:
                    speak('What should I say? ')
                    content = myCommand()
        
                    server = smtplib.SMTP('smtp.gmail.com', 587)
                    server.ehlo()
                    server.starttls()
                    server.login("Your_Username", 'Your_Password')
                    server.sendmail('Your_Username', "Recipient_Username", content)
                    server.close()
                    speak('Email sent!')

                except:
                    speak('Sorry Aiden! I am unable to send your message at this moment!')


        elif 'nothing' in query or 'abort' in query or 'stop' in query:
            speak('yes sir')
            speak('Bye Aiden, have a good day.')
            sys.exit()
           
        elif 'hello' in query:
            speak('Hello Aiden')

        elif 'bye' in query:
            speak('Bye Aiden, have a good day.')
            sys.exit()
                                    
        elif 'play music' in query:
            music_folder = Your_music_folder_path
            music = [music1, music2, music3, music4, music5]
            random_music = music_folder + random.choice(music) + '.mp3'
            os.system(random_music)
                  
            speak('yes sir, here is your music! Enjoy!')

        elif "dinner" in query:
            foods = ['com llq','com tc','banh canh','hu tieu nam vang','ga ran','pho','bot chien' ]
            num_of_food=len(foods)
            randomNumber = random.randint(0,num_of_food -1 )
            speak("I have a suggestion for you, how about " + foods[randomNumber + "?"])
        elif "weather" in query and ("now" or "today") in query:
            response = requests.get('https://api.darksky.net/forecast/24cd61bddf35c80d5e2ff15663b50ec8/10.776530,106.700981')
            json_data = json.loads(response.text)
            summary = json_data['currently']['summary']
            #Calculate F to C
            temC = (json_data['currently']['temperature']-32)*5/9
            speak("the weather is {} and the temperature is {} degree celcius".format(summary,str(round(temC,2))))
        elif 'your name' in query:
             speak('I am Jarvis, your personal assistant')
         
        else:
            query = query
            speak('Searching...')
            try:
                try:
                    res = client.query(query)
                    results = next(res.results).text
                    speak('WOLFRAM-ALPHA says - ')
                    speak('Got it.')
                    speak(results)

                except:
                    results = wikipedia.summary(query, sentences=2)
                    speak('Got it.')
                    speak('WIKIPEDIA says - ')
                    speak(results)

            except:
                webbrowser.open('www.google.com')



        speak('Next Command! Sir!')
