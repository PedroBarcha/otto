lexicon="/home/anshee/Documents/projects/otto/lexica/otto-lexicon.txt"
phrase="ai meu coco ta doendo"

words=phrase.split()	

with open(lexicon) as f:
    for line in f:
    	coco=line.split()
    	if (coco[0] in words):
    		print ("caquita")