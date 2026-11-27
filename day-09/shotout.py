# import pyttsx3

# engine = pyttsx3.init()
# names = ["Ali", "Sara", "Zain", "Ayesha"]

# for name in names:
#     engine.say(f"Shoutout to {name}!")

# engine.runAndWait()

import win32com.client

speaker = win32com.client.Dispatch("SAPI.SpVoice")
names = ["Ali", "Sara", "Zain"]

for name in names:
    speaker.Speak(f"Shoutout to {name}")
