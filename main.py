import time

from voice.speak import speak
from voice.listen import listen
from brain.commands import process_command

def main():
    speak("Zara online")

    while True:
        command = listen()
        print("Heard:", command)
        response = process_command(command)
        time.sleep(0.5)
        print("response:",response)
        speak(response)
        if "bye" in response:
            break

if __name__ == "__main__":
    main()