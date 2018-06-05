#send the audio to the ibm api and get their json response

from __future__ import print_function
from io import StringIO
import json
from os.path import join, dirname
from watson_developer_cloud import SpeechToTextV1

#full path to the user record
audio_path="/home/anshee/Documents/projects/otto/records/user.wav"

speech_to_text = SpeechToTextV1(
    	username="87bc7b23-450f-4070-94e4-359ffa926bb7",
    	password="khFUoo6D2I71",
    	url='https://stream.watsonplatform.net/speech-to-text/api')

def stt():
	stt_raw_json = StringIO() #stt=speech-to-text
	with open(join(dirname(__file__), audio_path),'rb') as audio_file:
		json.dump(speech_to_text.recognize(audio=audio_file, content_type='audio/ogg'), stt_raw_json)

	#extract the transcript out of the json
	stt_str_json=(json.loads(stt_raw_json.getvalue()))
	transcript=stt_str_json["results"][0]["alternatives"][0]["transcript"]
	print ("\nTRANSCRIPTION: "+transcript+"\n")
	return transcript