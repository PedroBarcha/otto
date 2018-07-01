import RPi.GPIO as GPIO
import time
def send(emotion):
    gpio=mapEmotion(emotion)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup([29,31,33,35],GPIO.OUT)
    GPIO.output(35,GPIO.HIGH) #ce
    GPIO.output(33,gpio[0]) #bit1
    GPIO.output(31,gpio[1]) #bit2
    GPIO.output(29,gpio[2]) #bit3
    
    
def mapEmotion(emotion):
    gpio = []
    if(emotion.lower()=="joy" ):
        gpio.append(GPIO.HIGH)
        gpio.append(GPIO.LOW)
        gpio.append(GPIO.LOW)
        return gpio
    if(emotion=="Sadness"): return
        
    if(emotion=="Fear"): return
        
    if(emotion=="Disgust"): return
       
    if(emotion=="Anger"): return
        
    
def turnOff():
    GPIO.output(35,GPIO.LOW) #ce

    

