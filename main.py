from gtts import gTTS
import os

# your text witch you want to convert to mp3
mytext = "Hello World"

# your language in witch you want co convert to mp3
language = "en"

myobj = gTTS(text=mytext, lang=language, slow=False)


# Method to create your audio file in mp3 format
myobj.save("hello-world.mp3")
print("Audio Saved!")