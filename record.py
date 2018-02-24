import pyaudio
import os
import wave

FORMAT = pyaudio.paInt16

# Keep number of channel one to avoid errors in speech api like retry error
CHANNELS = 1
RATE = 44100
CHUNK = 1024
RECORD_SECONDS = 10
WAVE_OUTPUT_FILENAME = "file.wav"
FLAC_OUTPUT_FILENAME = 'file.flac'
PATH_TO_AUDIO_FILE = os.path.dirname(os.path.abspath(__file__))

def record_audio():
    audio = pyaudio.PyAudio()

    # starts Recording
    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)
    print("Please say something......")
    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("Thank you for Input")

    # stop Recording
    stream.stop_stream()
    stream.close()
    audio.terminate()

# get current directory and save recorded file in that directory
    path = PATH_TO_AUDIO_FILE
    path = path + '\\' + WAVE_OUTPUT_FILENAME
    print(path)
    waveFile = wave.open(path, 'wb')
    waveFile.setnchannels(CHANNELS)
    waveFile.setsampwidth(audio.get_sample_size(FORMAT))
    waveFile.setframerate(RATE)
    waveFile.writeframes(b''.join(frames))
    waveFile.close()

    play = pyaudio.PyAudio()
    stream_play = play.open(format=FORMAT,
                            channels=CHANNELS,
                            rate=RATE,
                            output=True)

    # Gives Output of recording
    for data in frames:
        stream_play.write(data)
    stream_play.stop_stream()
    stream_play.close()
    play.terminate()

# executes this code if script is executed directly in cmd or pycharm
if __name__ == "__main__":
    record_audio()