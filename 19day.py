# smtplib module
# ------------------
# this provides a client to sending emails via the simple mail transfer protocol(smtp)


# import smtplib
# from email.message import EmailMessage
# sender_email="anushadarapureddi3@gmail.com"
# password="bkqc fkkv qujq mqkj"
 
# reciever_email="anasuyadarapureddi@gmail.com"
# msg=EmailMessage()
# msg['Subject']="python Email Automaation"
# msg['From']=sender_email
# msg['To']=reciever_email
# msg.set_content("Hello ,this email is sent using python")
# server=smtplib.SMTP_SSL('smtp.gmail.com',465)
# server.login(sender_email,password)
# server.send_message(msg)
# server.quit()
# print("email sent successfully")


import pyttsx3
import speech_recognition as sr
import datetime
import webbrowser
import wikipedia
 
 #initialise voice engine
engine=pyttsx3.init()
def speak(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    recognizer=sr.Recognizer()
    
    with sr.Microphone() as source:
        print("listening")
        recognizer.pause_threshold=1
        audio=recognizer.listen(source)
    try:
        print("recognising")
        command=recognizer.recognize_google(audio)
        print("you said",command)
        return command.lower()
    except Exception:
        print("sorry,please say that again")
        return ""
def wish_user():
    hour=datetime.datetime.now().hour
    if hour<12:
        speak("good morning")
    elif hour<18:
        speak("good afternoon")
    else:
        speak("good evening")
    speak("iam your virtual assistant")
wish_user()
while True:
    command=take_command()
    if "time" in command:
        time=datetime.datetime.now().strftime("%I:%M %p")
        speak(f"The time is {time}")
    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
    elif "open google" in command:
        webbrowser.open("https://www.google.com")
    elif "who is" in command:
        person=command.replace("who is " "")
        info=wikipedia.summary(person,2)
        print(info)
        speak(info)
    elif "exit" in command:
        speak("goodbye")
        break