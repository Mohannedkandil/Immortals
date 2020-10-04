import time
import requests
import pyttsx3
import speech_recognition as sr
import cv2

cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
ret, frame = cap.read()


def speak(text):
    engine = pyttsx3.init()
    newVoiceRate = 140
    engine.setProperty('rate', newVoiceRate)
    engine.say(text)
    engine.runAndWait()
def camera():
    while(True):
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        cap.release()
        cv2.destroyAllWindows()


r = sr.Recognizer()
# Reading Microphone as source
# listening the speech and store in audio_text variable
cnt = 0
tw = ['twitter','Twitter','Tweet','tweet']
tw2 = []
with sr.Microphone() as source:
    print("Talk")
    audio_text = r.listen(source)
    print("Time over, thanks")
    # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling

    cnt = cnt+1
    # using google speech recognition
    print("Text: " + r.recognize_google(audio_text))
    text = r.recognize_google(audio_text)
    if 'Twitter' in text:
        r = requests.post('https://maker.ifttt.com/trigger/post_twitter/with/key/kQlfN4tVuAI8ENmf800AGUHoaYDrqdDwD2cBqpUxc0j',
                            params={"value1": str(cnt), "value2": "none", "value3": "none"})
        speak("Your tweet about your first day on mars is published")

    if 'open camera' in text:
        speak("Your camera is open")
        cv2.imshwo('Main Window', frame)
        camera()

    if 'ISS' in text:
        speak("The Latest ISS on-orbit report is in your IOS Reading list")

        r = requests.post(
            'https://maker.ifttt.com/trigger/post/with/key/kQlfN4tVuAI8ENmf800AGUHoaYDrqdDwD2cBqpUxc0j',
            params={"value1": "none", "value2": "none", "value3": "none"})

