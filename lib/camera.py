from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2
import sys
import imutils

# Get user supplied values
cascPath1 = '/home/pi/Desktop/otto/face-models/haarcascade_frontalface_default.xml'
cascPath2= '/home/pi/Desktop/otto/face-models/haarcascade_profileface.xml'

def detectFaces(camera_stop, camera_emotion):
    try:
        #block execution while no signal arrives
        camera_stop.get()
        
        # Create the haar cascade
        faceCascade1 = cv2.CascadeClassifier(cascPath1)
        faceCascade2 = cv2.CascadeClassifier(cascPath2)
        
        consecutive_frontals=0
        consecutive_profiles=0

        # initialize the camera and grab a reference to the raw camera capture
        camera = PiCamera()
        camera.resolution = (160, 128)
        camera.framerate = 32
        rawCapture = PiRGBArray(camera, size=(160, 128))

        # allow the camera to warmup
        time.sleep(0.1)
        ignoring_toleration=60 #if you dont look at otto for this time he will get so angry at you! 
        t_start=time.time()

        for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
            print ("camera recording!")
            # capture frames from the camera until it gets a stop signal
            if (camera_stop.empty()):
                # grab the raw NumPy array representing the image, then initialize the timestamp
                # and occupied/unoccupied text
                image = frame.array
                gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
                    
                # Detect frontal faces in the image
                faces1 = faceCascade1.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
                )
                
                #if you look at otto, he gets happy
                frontals=len(faces1)
                if (frontals>0):
                    print "Found {0} FRONTAL(S)!".format(frontals)
                    consecutive_frontals+=1
                    if (consecutive_frontals>5):
                        print("Your gave attention to otto!")
                        consecutive_frontals=0
                        if (camera_emotion.empty()):
                            camera_emotion.put("joy")
                else:
                    consecutive_frontals=0

                # Detect profile faces in the image
                faces2 = faceCascade2.detectMultiScale(
                gray,
                scaleFactor=1.1,
                minNeighbors=5,
                minSize=(30, 30),
                flags = cv2.cv.CV_HAAR_SCALE_IMAGE
                )
                
                #if you turn your face to otto, he gets angry
                profiles=len(faces2)
                if (profiles>0):
                    print "Found {0} PROFILES(S)!".format(profiles)
                    consecutive_profiles+=1
                    if (consecutive_profiles>3):
                        print("Your turned your face to otto!")
                        consecutive_profiles=0
                        if (camera_emotion.empty()):
                            camera_emotion.put("anger")
                else:
                    consecutive_profiles=0
                    
                #if you dont look at otto for too long he will get so angry at you!
                if (((time.time()-t_start)>ignoring_toleration) and camera_emotion.empty()):
                    camera_emotion.put("sadness")    
        
            #stop signal received
            else:
                stop=camera_stop.get() #get the stop signal off the queue
                
                #start recording again
                if (stop==False):
                    camera_stop.get() #block execution
                    consecutive_frontals=0
                    consecutive_profiles=0
                    t_start=time.time()
                
                #otto is retired
                else:
                    return
                
            rawCapture.truncate(0)
            
                
    #terminate thread when keyboard interrupts occur
    except(KeyboardInterrupt, SystemExit):
        print("Wrapping camera thread up...")
        sys.exit()

