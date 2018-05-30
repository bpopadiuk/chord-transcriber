import pylab
from scipy.io import wavfile

def process_wav():
    sampleRate, data = wavfile.read('output.wav')
    data  = data / (2.**15)
    channel1 = data[:,0]

    return channel1
