from datetime import datetime
import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import pyttsx3
import wikipedia
import webbrowser


engine = pyttsx3.init()





name = "FEB"
owner = "Gaurav"


pyttsx3.speak("Enter Username")
who = input("Enter Username : ")
# who = who.lower()

def take_input():
    i = input(f"{who} : ")
    i = i.lower()                
    return i

def open_facebook():
    Facebook = webbrowser.open("https://facebook.com")
    return Facebook
                    
def open_google():
    Google = webbrowser.open("https://google.com")
    return Google

def open_youtube():
    youtube = webbrowser.open("https://youtube.com")
    return youtube

def get_time():
    now = datetime.now()
    current_time = now.strftime("Time is %H hours :%M minutes")
    return current_time

def get_date():
    today = datetime.date.today()
    return today

def need_Help():
    h1 = {"For Google" : "Type open Google",
    "For youtube" : "open Youtube",
    "For Wikipedia" : "Search on wikipedia",
    "For Facebook" : "Open facebook" }
    return h1

def process(i):
    if "what is your name" in i:
        return (f"I'm {name}")


    elif "open youtube" in i:
                y = input("Search on YouTube : ")
                youtube = webbrowser.open(f"https://www.youtube.com/results?search_query={y}")
                return (f"Opening Youtube and Searching for {y}", youtube)

    elif "search on wikipedia" in i:
        w = input("Search on Wikipedia : ")
        result = wikipedia.summary(w, sentences = 2)
        return (result)
                
    elif "H" in i:
        pyttsx3.speak("What can i do for you, I can you these things listed below ")
        print(" I can search for you on Google\n I can Youtube videos\n I can  Search on wikipedia\n I can Open facebook\n I can tell you time and many more things" )
        pyttsx3.speak(" I can search for you on Google\n I can Youtube videos\n I can Search on wikipedia\n I can Open facebook\n I can tell you time and many more things")
        return need_Help()


    elif "open google" in i:
        G = input("Search On Google : ")
        Google = webbrowser.open(f"https://www.google.com/search?safe=active&sxsrf=ALeKk01XkYHYU_LybPAGDea0-3ySMgrd6g:1615348355829&q={G}&spell=1&sa=X&ved=2ahUKEwj30r_H6aTvAhXoFLcAHfQODBgQBSgAegQIBhBT&biw=1163&bih=560#scso=_ikJIYJ-3NcHZz7sPwJOFmA831:12.727272033691406")
        return (f"Opening Google and Searching for {G}" , Google)
                

    elif "open facebook" in i:
        return (f"Opening Facebook {open_facebook()}" )

    elif "date" in i:
        return (get_date)
                
    elif ("what is time") in i:
        return (get_time())

    elif ("Sachin Tendulkar") in i:
        return ("Sachin Tendulkar is the India's Best criketer")
            
    elif ("owner") in i:
        return (f"My creator is {owner} , so He is my Owner")


    else:
        print("Sorry! Could not Recoginize")



if who == "Gaurav":
    pyttsx3.speak("Enter Password")
    password = input("Enter Password : ")
    if password == "9870":

        pyttsx3.speak("Welcom Gaurav")

        while(True):
            i = take_input()
            o = process(i)
            print(f"{name} : {o}")

            engine = pyttsx3.init()
            engine.say(o)
            engine.runAndWait

            pyttsx3.speak("What can I do for you Master")


    else:
        print("Wrong Password")
        pyttsx3.speak("I think you forget the password")
        pyttsx3.speak("you can only try two more times")
        pyttsx3.speak("Try again")
        password1 = input("Enter Password Again : ")
        if password1 == "9870":

            pyttsx3.speak("Welcom Gaurav")

            while(True):
                i = take_input()
                o = process(i)
                print(f"{name} : {o}")

                engine = pyttsx3.init()
                engine.say(o)
                engine.runAndWait

                pyttsx3.speak("What can I do for you Master")
        else:
            print("Wrong Password")
            pyttsx3.speak("I think you forget the password")
            pyttsx3.speak("Last one attempt left")
            pyttsx3.speak("Try again")
            password1 = input("Enter Password Again : ")
            if password1 == "9870":

                pyttsx3.speak("Welcom Gaurav")
                
                while(True):
                    i = take_input()
                    o = process(i)
                    print(f"{name} : {o}")

                    engine = pyttsx3.init()
                    engine.say(o)
                    engine.runAndWait

                    pyttsx3.speak("What can I do for you Master")

            else:
                pyttsx3.speak("wrong password")
                Print("Wrong Password")

                

else:
    pyttsx3.speak("Closing The Program")
    pyttsx3.speak("You are not an Authorized User")
    print("You are not an Authorized User")

                    
                    
           