import os
import eel
import subprocess  # Import subprocess module

from engine.features import *
from engine.command import *
from engine.auth import recognize  # Correct the import if it's a typo

def start():
    
    eel.init("www")

    playAssistantSound()  # Ensure this function is defined or imported
    @eel.expose
    def init():
        subprocess.call([r'device.bat'])
        eel.hideLoader()
        speak("Ready for Face Authentication")  # Ensure this function is defined or imported
        flag = recognize.AuthenticateFace()  # Correct the function call if it's a typo
        if flag == 1:
            eel.hideFaceAuth()
            speak("Face Authentication Successful")
            eel.hideFaceAuthSuccess()
            speak("Hello, Welcome Sir, How can i Help You")
            eel.hideStart()
            playAssistantSound()
        else:
            speak("Face Authentication Fail")
    os.system('start chrome.exe --app="http://localhost:8000/index.html"')

    eel.start('index.html', mode=None, host='localhost', block=True)