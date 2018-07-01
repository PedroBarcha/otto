#output handler
from lib import toArd
import vlc
import time
import os

sounds_path= '/home/pi/Desktop/otto/sounds/'

#otto makes a different sound according to the emotion recognized
def sound(emotion):
        toArd.send(emotion)
        p = vlc.MediaPlayer(sounds_path+emotion.lower()+".mp3")
	p.play()
	time.sleep(6) #necessary otherwise the whole sound might not be played
	toArd.turnOff()

###################################
#other kinds of outputs go here too
###################################
