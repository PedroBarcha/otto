#output handler

import vlc
import time
import os

sounds_path= '/home/pi/Desktop/otto/sounds/'

#otto makes a different sound according to the emotion recognized
def sound(emotion):
	p = vlc.MediaPlayer(sounds_path+emotion.lower()+".mp3")
	p.play()
	time.sleep(4) #necessary otherwise the whole sound might not be played

###################################
#other kinds of outputs go here too
###################################
