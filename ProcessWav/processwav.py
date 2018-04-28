import pylab
from scipy.io import wavfile

def process_wav():
    sampFreq, snd = wavfile.read('output.wav')
    snd = snd / (2.**15)
    s1 = snd[:,0]

    timeArray = pylab.arange(0, snd.shape[0], 1)
    timeArray = timeArray / sampFreq
    timeArray = timeArray * 1000 # scale to milliseconds
#    print('snd: ', snd)
    return s1


if __name__ == '__main__':
    sampFreq, snd = wavfile.read('output.wav')

#    snd = snd / (2.**15)
    s1 = snd[:,0]

    timeArray = pylab.arange(0, snd.shape[0], 1)
    timeArray = timeArray / sampFreq
    timeArray = timeArray * 1000 # scale to milliseconds

    pylab.plot(timeArray, s1, color='k')
    pylab.ylabel('Amplitude')
    pylab.xlabel('Time (ms)')
#    pylab.ylim(-.1, .1)
    pylab.show()
