## :octopus: Otto, The Emotional Toy
Ottos is a toy/robot (made with Raspbeey Pi and Arduino) that expresses emotions (anger, sadness, joy, fear and disgust) according to how the user interacts with her. Interactions can be via:
1. Audio: you can say anything you want to Otto! She will understand it and react accordingly.
2. Video: if you give Otto attention, she will be happy, otherwise she will be very sad 🙇.

Outputs are:
1. Moving: Otto can rotate and move 2 tentacles in order to express her emotions.
2. Lights: Otto has led strips inside her tentacles.
3. Eyes: Ottos has 2 [led displays](https://learn.adafruit.com/animated-electronic-eyes-using-teensy-3-1/overview) that can display several eyes templates.
4. Sound: sound reactions, through speakers.

## :space_invader: SETUP
1. Ensure to change the paths at otto_output.py, tone_analyzer, record and speech_to_text to where you cloned the repo.
2. python otto.py

## 💈 TODO
- [ ] *README* update hardware parts and schematics
- [ ] *README* update dependencies
- [ ] *README* upload a nice video
- [ ] *otto_output.py, tone_analyzer, record and speech_to_text*: make dynamic paths for god's sake
- [ ] *record.py*: threads are cutting the first word said by the user
- [x] *record.py*: implement audio to variable (instead of audio to file) and benchmark the results
- [x] *record.py*: right now the recording lasts a fixed number of seconds. We still have to change it to make it listen constantly for input and recognize when the user starts to speak (possibly by saying "otto") and when (s)he finishes.
- [x] *record.py+speech_to_text*: benchmark stt time with several types of audio formats 
- [x] *speech_to_text.py*: benchmark regular stt vs stt with websockets. RES: regular method wins hands down
- [x] *tone_analyzer.py*: add priority lexicon
