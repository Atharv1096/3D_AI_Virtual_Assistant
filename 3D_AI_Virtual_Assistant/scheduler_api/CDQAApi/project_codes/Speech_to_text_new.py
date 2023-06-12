import speech_recognition as sr
import time

# Initialize recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Flag to indicate whether this is the first transcription
first_transcription = True

# Minimum audio frequency for detecting speech (adjust as needed)
min_speech_frequency = 200


def transcribe():
    print("Please speak into the microphone and press Enter to end the conversation: ")
    with sr.Microphone() as source:
        # Adjust microphone threshold dynamically
        r.adjust_for_ambient_noise(source)
        print("Adjusting microphone for ambient noise...")

        # Start the audio stream
        audio_stream = r.listen(source)

        # Variable to store the transcribed text
        text = ""

        # Variable to indicate if the user has stopped speaking
        stopped_speaking = False

        # Loop until the conversation is ended
        while not stopped_speaking:
            try:
                # Transcribe the audio
                text = r.recognize_google(audio_stream)
                print("Transcription:", text)
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print(
                    "Could not request results from Google Speech Recognition service; {0}".format(e))

            # Check if the user wants to end the conversation
            if text and text.lower() == "exit":
                print("Exiting the conversation.")
                break

            # Start a new audio stream
            audio_stream = r.listen(source, phrase_time_limit=1)

            # Check if the user has stopped speaking
            stopped_speaking = len(audio_stream.frame_data) == 0

        return text


# Capture and transcribe speech
while True:
    # Get transcription from the user
    text = transcribe()

    # Check if the user wants to end the conversation
    if text and text.lower() == "exit":
        break

    # Wait for 1 second before continuing
    time.sleep(1)
