import sounddevice as sd
import scipy.io.wavfile as wavfile
import speech_recognition as sr

def listen(duration=4):
    fs = 16000

    print("Zara is listening...")

    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()
    sd.stop()

    wavfile.write("temp.wav", fs, recording)

    recognizer = sr.Recognizer()

    with sr.AudioFile("temp.wav") as source:
        audio = recognizer.record(source)

    try:
        command = recognizer.recognize_google(audio)
        print("You said:", command)
        return command.lower()
    except:
        print("Couldn't understand")
        return ""