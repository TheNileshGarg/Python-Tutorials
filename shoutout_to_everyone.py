## Shoutout to everyone
# Write a program to pronounce list of names using win32 API. If you are given a list l as follows:
# l = ["Rahul", "Nishant", "Harry"]
# Your program should pronouce
# Shoutout to Rahul
# Shoutout to Nishant
# Shoutout to Harry

import time
import pyttsx3

def shoutout(names):
    engine = pyttsx3.init() 
    for name in names:
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[3].id)
        engine.say(f"Shoutout to {name}")
        engine.runAndWait() 
        time.sleep(1)
    
if __name__ == '__main__':
    shoutout(['Jake', 'Peter', 'Mike', 'Miachel', 'Andrew'])