import pylab
from scipy.io import wavfile

def process_wav():
    sampFreq, snd = wavfile.read('output.wav')
    snd = snd / (2.**15)
    s1 = snd[:,0]

#    timeArray = pylab.arange(0, snd.shape[0], 1)
#    timeArray = timeArray / sampFreq
#    timeArray = timeArray * 1000 # scale to milliseconds
    return s1
