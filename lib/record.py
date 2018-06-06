import pyaudio
import wave
import time
import audioop
import numpy
import threading

#audio variables
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100*2
CHUNK = 1024
WAVE_OUTPUT_FILENAME = "/home/anshee/Documents/projects/otto/records/user.wav"

silence_estimation_time=3
silence_threshold_factor=1.4
allowed_silence_time=0.6

user_speaking=0


#calculate ambient noise (silence)
def set_trs(stream):
	max_noise = 0
	volumes = []

	#get input volume during silence_estimation_time seconds
	print("\nEstimating ambient noise, please wait SILENTLY... ")
	t=time.time()
	while((time.time()-t<silence_estimation_time)):
		current_volume=audioop.rms(stream.read(CHUNK), 2)
		volumes.append(current_volume)

	max_noise = max(volumes)
	print ("Microphone ready!")

	return max_noise


def record():
	frames = []
	audio = pyaudio.PyAudio()

	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)

	#record while the user is still speaking
	while(user_speaking):
		for i in range(0, int(RATE/CHUNK)):
			data = stream.read(CHUNK)
			frames.append(data)

	#stop recording
	stream.stop_stream()
	stream.close()
	audio.terminate()

	#save audio file
	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()



def detectVoice():
	global user_speaking

	#set recording variables
	audio = pyaudio.PyAudio()
	stream1 = audio.open(format=FORMAT, channels=CHANNELS,
		                rate=RATE, input=True,
		                frames_per_buffer=CHUNK)
	
	#set record thread
	class myThread(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
		def run(self):
			record()
	
	#calculate silence threshold
	silence_threshold=set_trs(stream1)
	silence_threshold=silence_threshold*silence_threshold_factor

	#keep checking if the silence threshold is exceeded (some on is talking to #otto). when it happens, start recording (in a new thread)
	while (1):
		if(audioop.rms(stream1.read(CHUNK),2)>silence_threshold):
			user_speaking=1
			myThread=myThread()
			myThread.start()
			print("RECORDING...")
			break

	#record while there is no silence for more than allowed_silence_time
	flag=1
	while(flag):
		t=time.time()
		while (audioop.rms(stream1.read(CHUNK),2)<=silence_threshold):
			if (time.time()-t > allowed_silence_time ):
				flag=0
				user_speaking=0
				print("FINISHED RECORDING.")
				break

	#wait for recording file to be saved			
	myThread.join()






