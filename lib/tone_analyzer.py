import json
from watson_developer_cloud import ToneAnalyzerV3
from io import StringIO
import os

lexicon='/home/pi/Desktop/otto/lexica/otto-lexicon.txt'

tone_analyzer = ToneAnalyzerV3(
    username="065ec1b0-10a0-468d-a59f-3608faceecbf",
    password="fpAryMaxXfr2",
    version="2016-05-19")

#the words contained in otto-lexicon.txt are high-priority and have assigned #emotions. they must be checked before using the IBM tone analyer
def lexiconCheck(transcript):
	str_transcript=transcript.split()	

	#if the lexicon contains a word in the transcript, return the assigned #emotion
	with open(lexicon) as f:
		for line in f:
			word=line.split()
			if (word[0] in str_transcript):
				print ("LEXICON WORD FOUND: "+word[0])
				return word[1]

#ibm watson-tone-analyer api
def watsonToneAnalyzer(transcript):
	tone_raw_json = StringIO()
	tone_raw_json = json.dumps(tone_analyzer.tone(tone_input=transcript, content_type="text/plain"))

	#extract the emotions out of the json
	emotion="joy"
	score=0
	tone_str_json=(json.loads(tone_raw_json))
	for i in range (0,5):
		aux_score=tone_str_json["document_tone"]["tone_categories"][0]["tones"][i]["score"]
		aux_emotion=tone_str_json["document_tone"]["tone_categories"][0]["tones"][i]["tone_name"]
		print (aux_emotion+" => "+str(aux_score))

		#get maximum score emotion
		if (aux_score>score):
			score=aux_score
			emotion=aux_emotion
	
	return emotion

#first try the lexicon, if no word of it was used then use the ibm api
def getPredominantEmotion(transcript):
	emotion=lexiconCheck(transcript)
	if(emotion):
		print ("PREDOMINANT EMOTION: "+emotion+'\n')
		return emotion
	else:
		emotion=watsonToneAnalyzer(transcript)
		print ("\nPREDOMINANT EMOTION: "+emotion+'\n')
	return emotion
