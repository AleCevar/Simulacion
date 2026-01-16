#ifndef SIMULACION_GEOMETRIC_H
#define SIMULACION_GEOMETRIC_H

#include "../Header.h"
#include "Distribution.h"

class Geometric : public Distribution {
  private:
    double p;
    mt19937 gen;
    geometric_distribution<> dist;

  public:
    explicit Geometric(double p_) : p(p_) {
      random_device rd;
      gen = mt19937(rd());
      dist = geometric_distribution<>(p);
    }

    double generate() override {return dist(gen);}
};

#endif