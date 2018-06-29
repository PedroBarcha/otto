from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image
import time
import threading, Queue

#serial = i2c(port=0, address=0x3C)
serial1 = i2c(port=1, address=0x3C)

#device = sh1106(serial)
device1 = sh1106(serial1)
    
photo = Image.open("/home/pi/Desktop/otto/eyes/neutral.ppm")
#device.display(photo.convert(device.mode))
device1.display(photo.convert(device1.mode))

time.sleep(3)