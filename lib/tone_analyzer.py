#pass the transcript to the tone analyzer, which recognizes emotions;
#return predominat emotion

from __future__ import print_function
import json
from watson_developer_cloud import ToneAnalyzerV3
from io import StringIO

tone_analyzer = ToneAnalyzerV3(
    username="065ec1b0-10a0-468d-a59f-3608faceecbf",
    password="fpAryMaxXfr2",
    version="2016-05-19")

def getPredominantEmotion(transcript):
	tone_raw_json = StringIO()
	json.dump(tone_analyzer.tone(tone_input=transcript, content_type="text/plain"), tone_raw_json)

	#extract the emotions out of the json
	score=0
	tone_str_json=(json.loads(tone_raw_json.getvalue()))
	for i in range (0,5):
		aux_score=(tone_str_json["document_tone"]["tone_categories"][0]["tones"][i]["score"])
		aux_emotion=tone_str_json["document_tone"]["tone_categories"][0]["tones"][i]["tone_name"]
		print (aux_emotion+" => "+str(aux_score))

		#get maximum score emotion
		if (aux_score>score):
			score=aux_score
			emotion=aux_emotion

	print ("\nPREDOMINANT EMOTION: "+emotion+'\n')
	return emotion