import pyaudio
import wave
import time
import audioop
import numpy
import threading, Queue
import os
import time

#audio variables
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
WAVE_OUTPUT_FILENAME = '/home/pi/Desktop/speech_recognition2/otto/records/user.wav'

silence_estimation_time=3
silence_threshold_factor=1.4
allowed_silence_time=0.6

#calculate ambient noise (silence)
def get_trs():
    max_noise = 0
    volumes = []
	
    #set recording variables
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
		                rate=RATE, input=True,
		                frames_per_buffer=CHUNK)
	
    #get input volume during silence_estimation_time seconds
    print("\nEstimating ambient noise, please wait SILENTLY... ")
    t=time.time()
    while((time.time()-t<silence_estimation_time)):
	current_volume=audioop.rms(stream.read(CHUNK, exception_on_overflow =False), 2)
	volumes.append(current_volume)

    max_noise = max(volumes)
    silence_threshold=max_noise*silence_threshold_factor

    #stop recording
    stream.stop_stream()
    stream.close()
    audio.terminate()
        
    return silence_threshold


def record(data_shared, flag_shared):
    #set recording variables
    audio = pyaudio.PyAudio()
    frames = []
    # start Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                    rate=RATE, input=True,
                    frames_per_buffer=CHUNK)

    #record while the user is still speaking
    flag=1
    while(flag):
            for i in range(0, int(RATE/CHUNK)):
                data = stream.read(CHUNK, exception_on_overflow =False)
                frames.append(data)
                data_shared.put(data)
                flag = flag_shared.get() 
                if(flag == 0):
                    break
            
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


def detectVoice(silence_threshold):
    #set threads
    data_shared = Queue.Queue()
    flag_shared = Queue.Queue()
    flag_shared.put(1)

    #set recording variables
    audio = pyaudio.PyAudio()
    stream = audio.open(format=FORMAT, channels=CHANNELS,
		                rate=RATE, input=True,
		                frames_per_buffer=CHUNK)
    
    #keep checking if the silence threshold is exceeded (some on is talking to otto). when it happens, start recording (in a new thread)
    print ("Microphone ready!")
    while (1):
	    if(audioop.rms(stream.read(CHUNK,exception_on_overflow =False),2)>silence_threshold):
		    user_speaking=1
		    stream.stop_stream()
                    stream.close()
		    audio.terminate()
		    myThread=threading.Thread(target=record, args=(data_shared,flag_shared))
		    myThread.start()
		    break

    #record while there is no silence for more than allowed_silence_time
    user_speaking=1
    print("RECORDING")	
    while(user_speaking):
            flag_shared.put(1)
            data=data_shared.get()
	    t=time.time()
	    i=0
	    while (audioop.rms(data,2) <= silence_threshold):
                    i=i+1
		    if (time.time()-t > allowed_silence_time ):
                            print(" RECORDING FINSHED")
			    flag_shared.put(0)
			    user_speaking=0
			    break
		    flag_shared.put(1)
		    data=data_shared.get()

    #wait for recording file to be saved
    myThread.join()
