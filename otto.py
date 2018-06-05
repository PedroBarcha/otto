###############################################################################
#Otto is an emotional robot that answers accordingly to what you say to her
###############################################################################
from lib import record, speech_to_text, tone_analyzer, output
import time

#record what user has to say and save to ./records/user-record.wav
record.detectVoice()
t1=time.time()

#send the audio to the ibm speech-to-text api and get their json response
transcript=speech_to_text.stt()
t2=time.time()
print("STT TIME: "+str(t2-t1))

#use otto-lexicon and ibm tone-analyzer to get the emotion
emotion=tone_analyzer.getPredominantEmotion(transcript)
t3=time.time()
print("EMOTION TIME: "+str(t3-t2))

output.sound(emotion)