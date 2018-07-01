from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image
import time
import threading, Queue

def displayEyes(eyes_on, eyes_emotion):
    serial = i2c(port=1, address=0x3C)
    device = sh1106(serial)

    #block when there is no signal telling the eyes to work
    while(eyes_on.get()!=False):
        emotion=eyes_emotion.get().lower()
        
        #thinking emotion is composed of two images swapping
        if (emotion=="thinking"):
            while(eyes_on.empty()):
                photo = Image.open("/home/pi/Desktop/otto/eyes/thinking.ppm")
                device.display(photo.convert(device.mode))
                time.sleep(0.4)
                photo = Image.open("/home/pi/Desktop/otto/eyes/neutral.ppm")
                device.display(photo.convert(device.mode))
                time.sleep(0.4)
	else:
            photo = Image.open("/home/pi/Desktop/otto/eyes/"+emotion+".ppm")
            device.display(photo.convert(device.mode))