def process_command(command):
    if "open youtube" in command:
        import webbrowser
        webbrowser.open("https://youtube.com")
        return "Opening YouTube"

    elif "open google" in command:
        import webbrowser
        webbrowser.open("https://google.com")
        return "Opening Google"

    elif "your name" in command:
        return "I am Zara, your assistant"
    if "zara" in command:
        return "Yes"
    if "enough" in command:
        return "Yes sir bye"


    else:
        return "I didn't understand"