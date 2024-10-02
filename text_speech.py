import pyttsx3
engine = pyttsx3.init()

text = input("enter text : ")

engine.say(text)

engine.runAndWait()