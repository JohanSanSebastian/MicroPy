# Importing necessary libraries
import sounddevice as sd
from numpy import linalg as LA
import numpy as np
import keyboard

# Defining the function that listens to the dB value of your mic and executes unmute and mute respectively
def microphone_control(indata, outdata, frames, time, status):
    volume_norm = np.linalg.norm(indata)*10
    print(int(volume_norm))

    dbVal = int(volume_norm)
    is_unmute = False

    if dbVal < 30:
        if is_unmute is True:
            keyboard.press_and_release('ctrl + d')
            is_unmute = False
    else:
        if is_unmute is False:
            keyboard.press_and_release('ctrl + d')
            is_unmute = True
