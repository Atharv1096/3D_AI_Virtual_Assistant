import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to transcribe speech


def transcribe():
    print("Please speak in the microphone and to end the conversation click enter: ")
    with sr.Microphone() as source:
        # listen for audio
        audio = r.listen(source)
        try:
            # transcribe audio
            text = r.recognize_google(audio)
            # clear first_transcription flag
            first_transcription = False
            return text
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
            return None
        except sr.RequestError as e:
            print(
                "Could not request results from Google Speech Recognition service; {0}".format(e))
            return None


# Capture and transcribe speech



"""import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Flag to indicate whether this is the first transcription
first_transcription = True


def callback(recognizer, audio):
    global first_transcription
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        text = recognizer.recognize_google(audio)
        # write transcribed text to file
        with open("output.txt", "w" if first_transcription else "a") as f:
            f.write(text + "\n")
        # clear first_transcription flag
        first_transcription = False
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print(
            "Could not request results from Google Speech Recognition service; {0}".format(e))


# start listening in the background
while True:

    stop_listening = r.listen_in_background(sr.Microphone(), callback)

    # wait for the user to stop the program
    input("Press any key to stop the program...")

    # stop listening
    stop_listening(wait_for_stop=False)"""
