from gtts import gTTS
import pyglet


def text_to_speech(textin):
    tts = gTTS(text=textin, lang='en')
    tts.save('file.mp3')

    try:
        pyglet.lib.load_library("C:\\Windows\\System32\\avbin64.dll")
        pyglet.have_avbin = True
        song = pyglet.media.load('file.mp3')  # your file name
        song.play()
        pyglet.app.run()
    except Exception as e:
        print("Ignoring exception", e)

