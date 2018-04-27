#include <stdio.h>
#include <stdlib.h>
#include <math.h>


#define A440 9

// computes the modular note degree (0-11) for a frequency f_n
int compute_note(double f_n) {
    double f_0 = 440.0;        // A = 440 Hz
    double a = 1.059463094359; // (2)^1/12
    double half_steps_away = (log10(f_n/f_0)) / (log10(a));
    double rounded = round(A440 + half_steps_away);
    double modrounded = fmod(rounded, 12);
    if(modrounded < 0)
        modrounded += 12;
    double note_degree = fmod(modrounded, 12);
    return (int) note_degree;
}

int main(int argc, char **argv) {
    int note_degree;
    double frequency = atof(argv[1]);

    note_degree = compute_note(frequency);
    printf("note degree of %.2lf Hz: %d\n", frequency, note_degree);
}
