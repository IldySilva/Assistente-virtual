import pyttsx3 

speaker=pyttsx3.init()
v=speaker.getProperty("voice")
print(v)
speaker.setProperty("voice",speaker.getProperty("voices")[0].id)


def speak(speech):
    speaker.say(speech)
    speaker.runAndWait()

speak("HI there")