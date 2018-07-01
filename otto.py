###############################################################################
#Otto is an emotional robot that answers accordingly to what you say to her
###############################################################################
from lib import record, speech_to_text, tone_analyzer, eyes, camera, output , toArd
import threading, Queue
import sys

#calculate ambient silence threshold
silence_threshold=record.get_trs()

#set eyes thread and display default eyes
#NOTES:-this thread keeps running until the end of the program.
#      -to change eyes_emotion, eyes_on.put(on) needs to be issued first
eyes_on=Queue.Queue()
eyes_emotion=Queue.Queue()
eyes_on.put(True)
eyes_emotion.put("neutral")
eyes_thr=threading.Thread(target=eyes.displayEyes, args=(eyes_on, eyes_emotion))
eyes_thr.start()

#set camera thread
#NOTE: -this thread on/off is triggered with a camera_stop.put(bool)
camera_stop=Queue.Queue()
camera_emotion=Queue.Queue()
#camera_thr=threading.Thread(target=camera.detectFaces, args=(camera_stop, camera_emotion))
#camera_thr.start()



while (1):
    try:
        #start looking for faces
        camera_stop.put(False)
                
        #record what the user has to say and save to ./records/user-record.wav
        record.detectVoice(silence_threshold, camera_emotion)
        
        camera_stop.put(False)

        #if camera got emotion
        if (not camera_emotion.empty()):
            emotion=camera_emotion.get()

        #if the microphone got emotion
        else:
            #send the audio to the ibm speech-to-text api and get their json response
            transcript=speech_to_text.stt()
            #if noise was recorded, record again
            if (transcript == False): 
                continue

            #use otto-lexicon and ibm tone-analyzer to get the emotion
            emotion=tone_analyzer.getPredominantEmotion(transcript)
        
        
	#otto reacts with his eyes
	eyes_emotion.put(emotion)
	eyes_on.put(True)

        #otto's sound reaction
        output.sound(emotion)

	#get back to default eyes state
	eyes_emotion.put("neutral")
        eyes_on.put(True)
        
    #terminate threads when keyboard interrupts occur
    except(KeyboardInterrupt, SystemExit):
        print("Wrapping eyes thread up...")
        eyes_on.put(False)
        camera_stop.put(True)
        eyes_thr.join()
        camera_thr.join()
        sys.exit()
