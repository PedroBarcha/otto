###############################################################################
#Otto is an emotional robot that answers accordingly to what you say to her
###############################################################################
from lib import record, speech_to_text, tone_analyzer, eyes, output
import threading, Queue
import sys

#calculate ambient silence threshold
silence_threshold=record.get_trs()

while (1):
    try:
        #display default eyes
        on=Queue.Queue()
        on.put(True)
        default_eyes_thr=threading.Thread(target=eyes.defaultEyes, args=(on,))
        default_eyes_thr.start()

        #record what user has to say and save to ./records/user-record.wav
        record.detectVoice(silence_threshold)
        print ("nois nem ta aqui")
        #send the audio to the ibm speech-to-text api and get their json response
        transcript=speech_to_text.stt()
        #if noise was recorded, record again
        if (transcript == False): 
            continue

        #use otto-lexicon and ibm tone-analyzer to get the emotion
        emotion=tone_analyzer.getPredominantEmotion(transcript)

        #otto's sound reaction
        output.sound(emotion)

    except(KeyboardInterrupt, SystemExit):
        print("Wrapping threads up...")
        on.put(False)
        default_eyes_thr.join()
        print("Almoost...")
        sys.exit()
        print("Terminated")
