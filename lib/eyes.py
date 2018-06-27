from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image
import time
import threading, Queue

def displayEyes(eyes_on, eyes_emotion):
    print ("\n\n FIRST TIE PNELY")
    #rev.1 users set port=0
    #substitute spi(device=0, port=0) below if using that interface
    serial = i2c(port=1, address=0x3C)
    #serial1 = i2c(port=0, address=0x3C)

    #substitute ssd1331(...) or sh1106(...) below if using that device
    device = sh1106(serial)
    #device1 = sh1106(serial)

    #display emotion
    while(eyes_on.get_nowait()!=False):
	print("luterass")
	photo = Image.open("/home/pi/Desktop/otto/eyes/"+eyes_emotion.get())
	print("\n\nCARREGOU")
        device.display(photo.convert(device.mode))
	print("\n\n\nPRINTOU")

    print ("\n\n\n\nFUDEU CARAIO")
