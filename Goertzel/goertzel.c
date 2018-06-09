#include <stdio.h>

int goertzel(double numSamples, int targetFreq) {
    double scalingFactor = numSamples / 2.0;

    double k = (0.5 + ((numSamples * freq) / sampleRate));
    double w = (2.0 * math.pi / numSamples) * k;
    cosine = math.cos(w)
    sine = math.sin(w)
    coeff = 2.0 * cosine
    Q1 = 0
    Q2 = 0

    for i in range(int(numSamples)):
        Q0 = coeff * Q1 - Q2 + data[i]
        Q2 = Q1
        Q1 = Q0

    real = (Q1 - Q2 * cosine) / scalingFactor
    imag = (Q2 * sine) / scalingFactor
    freqMagnitude = math.sqrt(real**2 + imag**2)



}
