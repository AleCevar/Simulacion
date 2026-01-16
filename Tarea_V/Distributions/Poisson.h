#ifndef SIMULACION_POISSON_H
#define SIMULACION_POISSON_H

#include "../Header.h"
#include "Distribution.h"

class Poisson : public Distribution {
  private:
    double lambda;
    mt19937 gen;
    poisson_distribution<> dist;

  public:
    explicit Poisson(double lambda_) : lambda(lambda_) {
      random_device rd;
      gen = mt19937(rd());
      dist = poisson_distribution<>(lambda);
    }
    
    double generate() override {return dist(gen);}
};

#endif