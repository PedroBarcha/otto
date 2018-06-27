from luma.core.interface.serial import i2c, spi
from luma.core.render import canvas
from luma.oled.device import sh1106
from PIL import Image
import time

def defaultEyes(on):
    # rev.1 users set port=0
    # substitute spi(device=0, port=0) below if using that interface
    serial = i2c(port=1, address=0x3C)
    #serial1 = i2c(port=0, address=0x3C)

    # substitute ssd1331(...) or sh1106(...) below if using that device
    device = sh1106(serial)
    #device1 = sh1106(serial)

    photo = Image.open('/home/pi/Desktop/eyes/happy41.ppm')

    # display on screen for a few seconds
    while(on.get()==True):
        device.display(photo.convert(device.mode))

