#ifndef SIMULACION_BINOMIAL_H
#define SIMULACION_BINOMIAL_H

#include "../Header.h"
#include "Distribution.h"

class Binomial : public Distribution {
  private:
    int n;
    double p;
    mt19937 gen;
    binomial_distribution<> dist;

  public:
    explicit Binomial(int n_, double p_) : n(n_), p(p_) {
      random_device rd;
      gen = mt19937(rd());
      dist = binomial_distribution<>(n,p);
    }

    double generate() override {return dist(gen);}
};

#endif