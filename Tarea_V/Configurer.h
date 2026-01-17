#ifndef SIMULACION_ENTRADA_H
#define SIMULACION_ENTRADA_H

#include "Header.h"
#include "Entry.h"
#include "Servers/Station.h"
#include "Distributions/Exponential.h"
#include "Distributions/Normal.h"
#include "Distributions/Binomial.h"
#include "Distributions/Geometric.h"
#include "Distributions/Poisson.h"

class Run {
  private:
    const int times=100;
  public:

    Run(){}

    double run(vector<int>& assignation) {
      Exponential dri = Exponential(1/0.75);
      Normal fry = Normal(3, 1);
      Binomial des = Binomial(5,0.6);
      Geometric chi = Geometric(0.1);
      Exponential checkoutDis = Exponential(1/2.5);
      Binomial amountDis = Binomial(5, 2.0/5);
      Poisson arriveDis = Poisson(3);
      vector<Station> stations={
        Station("Drinks", assignation[1], &dri, 0.9),
        Station("Fryer", assignation[2], &fry , 0.7),
        Station("Desserts", assignation[3], &des , 0.25),
        Station("Chicken", assignation[4], &chi , 0.3)
      };
      Entry entry(&arriveDis, &amountDis, 
        &checkoutDis, stations, assignation[0]);
      entry.start();
      return entry.getEstadistics();
    }

    double simulate(vector<int> assignation){
      double sum = 0;
      for(int i = 0; i < times; i++){
        sum += run(assignation);
      }
      return sum / times;
    }

};

#endif