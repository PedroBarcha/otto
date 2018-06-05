import pyaudio
import wave
import time
import audioop
import numpy
import thread
import threading


FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100*2
CHUNK = 1024
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "/home/rax/Desktop/AirLab/otto/records/samples/user.wav"
flag2=0

threadLock = threading.Lock()
threads = []
 
def set_trs(stream):
	max_noise = 0
	volumes = []
	t=time.time()
	while((time.time()-t<5)):
		current_volume=audioop.rms(stream.read(CHUNK), 2)
		volumes.append(current_volume)
		print("noise : " + str(current_volume))
	max_noise = max(volumes)
	print ("max noise value : " + str(max_noise))
	return max_noise


def record():
	frames = []
	audio = pyaudio.PyAudio()

	# start Recording
	stream = audio.open(format=FORMAT, channels=CHANNELS,
	                rate=RATE, input=True,
	                frames_per_buffer=CHUNK)

	while(flag2==0):
		print("flag2222 : " + str(flag2))
		for i in range(0, int(RATE/CHUNK)):
			data = stream.read(CHUNK)
			frames.append(data)
	stream.stop_stream()
	stream.close()
	audio.terminate()

	waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
	waveFile.setnchannels(CHANNELS)
	waveFile.setsampwidth(audio.get_sample_size(FORMAT))
	waveFile.setframerate(RATE)
	waveFile.writeframes(b''.join(frames))
	waveFile.close()



def detectVoice():
	global flag2
	class myThread(threading.Thread):
		def __init__(self):
			threading.Thread.__init__(self)
		def run(self):
			global flag2
	 		record()

	audio1 = pyaudio.PyAudio()
	# start Recording
	stream1 = audio1.open(format=FORMAT, channels=CHANNELS,
		                rate=RATE, input=True,
		                frames_per_buffer=CHUNK)

	 


	THRESHOLD=set_trs(stream1)
	THRESHOLD=1.4*THRESHOLD
	flag=0

	while (1):
		if( audioop.rms(stream1.read(CHUNK),2) > THRESHOLD ):
			myThread = myThread()
			myThread.start()
			print "START RECORDING"
			break


	while(flag == 0):
		if( audioop.rms(stream1.read(CHUNK),2) > THRESHOLD ): 
			print "RECORDING.."
		else:
			t1=time.time()
			while (audioop.rms(stream1.read(CHUNK),2) <= THRESHOLD ):
				print "RECORDING SILENCE.."
				if (time.time()-t1 > 1 ):
					print "STOP"
					flag=1
					flag2=1
					print("flag2 : " + str(flag2))
					break
	for t in threads:
		t.join()
	print "Exiting Main Thread"






