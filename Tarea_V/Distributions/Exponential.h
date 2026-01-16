#ifndef SIMULACION_EXPONENTIAL_H
#define SIMULACION_EXPONENTIAL_H

#include "../Header.h"
#include "Distribution.h"

using namespace std;

class Exponential : public Distribution{
    private:
        double lambda;
        exponential_distribution<> dist;
        mt19937 gen;
    public:
        explicit Exponential(double media) : lambda(media) {
            random_device rd;
            gen = mt19937(rd());
            dist = exponential_distribution<>(lambda);
        }

        double generate() override {return dist(gen);}
};

#endif 