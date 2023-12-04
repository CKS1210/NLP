import speech_recognition as sr

def speech2Text(file):
    Audio_file = file
    r = sr.Recognizer()

    with sr.AudioFile(Audio_file) as source:
        audio = r.record(source)

    try:
        textdata = r.recognize_google(audio)
        print("Text data: " + textdata)
        return textdata

    except sr.UnknownValueError:
        print("Audio Error")

    except sr.RequestError as e:
        print("Could not request results from Google API, {0}".format(e))

