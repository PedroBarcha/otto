#send the audio to the ibm api and get their json response

from __future__ import print_function
from io import StringIO
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1
#from watson_developer_cloud.websocket import RecognizeCallback

#full path to the user record
audio_path="/home/anshee/Documents/projects/otto/records/user.wav"

speech_to_text = SpeechToTextV1(
    	username="87bc7b23-450f-4070-94e4-359ffa926bb7",
    	password="khFUoo6D2I71",
    	url='https://stream.watsonplatform.net/speech-to-text/api')

def stt():
	stt_raw_json = StringIO() #stt=speech-to-text
	with open(join(dirname(__file__), audio_path),'rb') as audio_file:
		json.dump(speech_to_text.recognize(audio=audio_file, content_type='audio/wav'), stt_raw_json)

	#extract the transcript out of the json
	stt_str_json=(json.loads(stt_raw_json.getvalue()))
	transcript=stt_str_json["results"][0]["alternatives"][0]["transcript"]
	print ("\nTRANSCRIPTION: "+transcript+"\n")
	return transcript


# Using websockets
#class MyRecognizeCallback(RecognizeCallback):
#    def __init__(self):
#        RecognizeCallback.__init__(self)

#    def on_transcription(self, transcript):
#        print(transcript)

#    def on_connected(self):
#        print('Connection was successful')

#    def on_error(self, error):
#        print('Error received: {}'.format(error))

#    def on_inactivity_timeout(self, error):
#        print('Inactivity timeout: {}'.format(error))

#    def on_listening(self):
#        print('Service is listening')

#    def on_transcription_complete(self):
#        print('Transcription completed')

#    def on_hypothesis(self, hypothesis):
#        print(hypothesis)

#mycallback = MyRecognizeCallback()
#with open(join(dirname(__file__), 'records/rip-cat.wav'),
#          'rb') as audio_file:
#    speech_to_text.recognize_with_websocket(
#audio=audio_file, recognize_callback=mycallback)