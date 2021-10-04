import os
import pyautogui
import time
import playsound
import speech_recognition as sr
from gtts import gTTS

def speak(text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)

def get_audio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)

        except Exception as e:
            print("Exception: " + str(e))
    
    return said


speak("Hello Anton and Malwina, what would you like to watch?")
movie = get_audio()

print(pyautogui.size())
currentMouseX, currentMouseY = pyautogui.position()
print(currentMouseX, currentMouseY)
time.sleep(5)
pyautogui.doubleClick(146, 69)
time.sleep(5)
pyautogui.click(2811, 107)
time.sleep(5)
pyautogui.write(movie, interval=0.25)
time.sleep(5)
pyautogui.click(322, 441)
time.sleep(5)
pyautogui.click(1490, 420)
time.sleep(10)
pyautogui.click(2782, 1848)

