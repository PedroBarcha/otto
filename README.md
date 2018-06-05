## :space_invader: SETUP
1. Ensure to change the paths at otto_output.py, tone_analyzer and speech_to_text
2. python otto.py

## :octopus: TODO
- [x] *record.py*: implement audio to variable (instead of audio to file) and benchmark the results
- [ ] *record.py*: right now the recording lasts a fixed number of seconds. We still have to change it to make it listen constantly for input and recognize when the user starts to speak (possibly by saying "otto") and when (s)he finishes.
- [x] *record.py+speech_to_text*: benchmark stt time with several types of audio formats 
- [x] *speech_to_text.py*: benchmark regular stt vs stt with websockets. RES: regular method wins hands down
- [x] *tone_analyzer.py*: add priority lexicon