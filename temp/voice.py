import speech_recognition as sr


def record_volume():
    r = sr.Recognizer()
    with sr.Microphone(device_index=1) as source:
        print("Listen...")
        audio = r.listen(source)

    query = r.recognize_google(audio, language="ru")
    print(query.lower(), type(query.lower()))


record_volume()