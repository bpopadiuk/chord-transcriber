#include <stdio.h>
#include <math.h>

#define PI 3.14159265359

int goertzel(double numSamples, double targetFreq, void *data, int sampleRate) {
    double scalingFactor = numSamples / 2.0;

    double k = (0.5 + ((numSamples * targetFreq) / sampleRate));
    double w = (2.0 * PI / numSamples) * k;
    double cosine = cos(w);
    double sine = sin(w);
    double coeff = 2.0 * cosine;
    double Q0 = 0;
    double Q1 = 0;
    double Q2 = 0;

    for(int i = 0; i < numSamples; i++) { 
        Q0 = coeff * Q1 - Q2 + data[i];
        Q2 = Q1;
        Q1 = Q0;
    }

    double real = (Q1 - Q2 * cosine) / scalingFactor;
    double imag = (Q2 * sine) / scalingFactor;
    double freqMagnitude = sqrt(real * real + imag * imag);

    return freqMagnitude;
}
