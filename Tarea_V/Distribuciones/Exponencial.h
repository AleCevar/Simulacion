#ifndef SIMULACION_EXPONENCIAL_H
#define SIMULACION_EXPONENCIAL_H

#include <random>
#include "Distribucion.h"

using namespace std;

class Exponencial : public Distribucion{
    private:
        double lambda;
        exponential_distribution<> dist;
        mt19937 gen;
    public:
        explicit Exponencial(double lambda_) : lambda(lambda_) {
            random_device rd;
            gen = mt19937(rd());
            dist = exponential_distribution<>(lambda);
        }

        double generar() override {return dist(gen);}
};

#endif SIMULACION_EXPONENCIAL_H