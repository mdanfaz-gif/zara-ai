import pyttsx3

def speak(text):
    print("Speaking:", text)

    engine = pyttsx3.init()   # ⭐ create fresh engine every time

    engine.setProperty('rate', 170)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice

    engine.say(text)
    engine.runAndWait()

    engine.stop()   # ⭐ VERY IMPORTANT