"""
Record 0.2 seconds of audio and save as a .wav file for processing.

CHUNK and RATE are unorthodox values at the moment. I'm playing with 
them to improve frequency resolution when processing the audio with
goertzel filters. I need to do more research to identify optimal 
values...
"""

import pyaudio
import wave

def capture(DEVICE):

    CHUNK = 16384
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 48000
    RECORD_SECONDS = 0.5
    WAVE_OUTPUT_FILENAME = "output.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                    channels=CHANNELS,
                    rate=RATE,
                    input=True,
                    input_device_index=DEVICE,
                    frames_per_buffer=CHUNK)

    print("listening...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("processing...")

    stream.stop_stream()
    stream.close()
    p.terminate()

    wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()

