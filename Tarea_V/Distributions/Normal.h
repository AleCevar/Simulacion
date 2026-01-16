#ifndef SIMULACION_NORMAL_H
#define SIMULACION_NORMAL_H

#include "../Header.h"
#include "Distribution.h"

class Normal : public Distribution {
  private:
    double mean;
    double stddev;
    mt19937 gen;
    normal_distribution<> dist;

  public:
    explicit Normal(double mean_, double stddev_) : mean(mean_), stddev(stddev_) {
      random_device rd;
      gen = mt19937(rd());
      dist = normal_distribution<>(mean,stddev);
    }

    double generate() override {return int(dist(gen)+1);} 
    // ojo negativos >:)
};

#endif