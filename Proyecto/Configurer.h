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
  public:

    Run(){}

    pair<double,double> run(vector<int>& assignation) {
      Exponential dri = Exponential(DRI_LAMBDA);
      Normal fry = Normal(FRY_MEAN, FRY_DESVIATION);
      Binomial des = Binomial(DES_N,DES_P);
      Geometric chi = Geometric(CHI_P);
      Exponential checkoutDis = Exponential(CHECKOUT_LAMBDA);
      Binomial amountDis = Binomial(AMOUNT_N, AMOUNT_P);
      Poisson arriveDis = Poisson(ARRIVE_LAMBDA);
      vector<Station> stations={
        Station(FIRST_NAME, assignation[1], &dri, FIRST_PROB),
        Station(SECOND_NAME, assignation[2], &fry , SECOND_PROB),
        Station(THIRD_NAME, assignation[3], &des , THIRD_PROB),
        Station(FOURTH_NAME, assignation[4], &chi , FOURTH_PROB)
      };
      Entry entry(&arriveDis, &amountDis, 
        &checkoutDis, stations, assignation[0]);
      entry.start();
      return entry.getEstadistics();
    }

    pair<double,double> simulate(vector<int> assignation, int times){
      double sum_mean = 0, sum_var = 0;
      for(int i = 0; i < times; i++){
        auto [mean,var] = run(assignation);
        sum_mean += mean;
        sum_var += var;
      }
      return {sum_mean / times, sum_var / times};
    }

    void runTests(){
      Exponential dri = Exponential(DRI_LAMBDA);
      Normal fry = Normal(FRY_MEAN, FRY_DESVIATION);
      Binomial des = Binomial(DES_N,DES_P);
      Geometric chi = Geometric(CHI_P);
      Exponential checkoutDis = Exponential(CHECKOUT_LAMBDA);
      Binomial amountDis = Binomial(AMOUNT_N, AMOUNT_P);
      Poisson arriveDis = Poisson(ARRIVE_LAMBDA);
      dri.test();
      cout<<'\n';
      fry.test();
      cout<<'\n';
      des.test();
      cout<<'\n';
      chi.test();
      cout<<'\n';
      checkoutDis.test();
      cout<<'\n';
      amountDis.test();
      cout<<'\n';
      arriveDis.test();
    }

};

#endif