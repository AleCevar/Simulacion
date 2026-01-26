#ifndef SIMULACION_ENTRADA_H
#define SIMULACION_ENTRADA_H

#include "ChartMaker.h"
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
    double percentil(vector<double> & v, double p) {
      int n = (int) v.size();
      double i = (p / 100.0) * (n - 1);
      int i0 = (int)i;
      int i1 = i0 + 1;
      assert(i0 < n);
      if (i1 >= n) return v[i0];
      double frac = i - i0;
      return v[i0] * (1 - frac) + v[i1] * frac;
    }

  public:

    Run(){}

    Statistic run(vector<int>& assignation, double checkLambda, double chickenProb) {
      Exponential dri = Exponential(DRI_LAMBDA);
      Normal fry = Normal(FRY_MEAN, FRY_DESVIATION);
      Binomial des = Binomial(DES_N,DES_P);
      Geometric chi = Geometric(CHI_P);
      Exponential checkoutDis = Exponential(checkLambda);
      Binomial amountDis = Binomial(AMOUNT_N, AMOUNT_P);
      Poisson arriveDis = Poisson(ARRIVE_LAMBDA);
      vector<Station> stations={
        Station(FIRST_NAME, assignation[1], &dri, FIRST_PROB),
        Station(SECOND_NAME, assignation[2], &fry , SECOND_PROB),
        Station(THIRD_NAME, assignation[3], &des , THIRD_PROB),
        Station(FOURTH_NAME, assignation[4], &chi , chickenProb)
      };
      Entry entry(&arriveDis, &amountDis, 
        &checkoutDis, stations, assignation[0]);
      entry.start();
      return entry.getAllStats();
    }

    pair<double,double> simulate(vector<int> assignation, int times = NUMBER_CYCLES, double checkoutLambda = CHECKOUT_LAMBDA, double chickenProb = FOURTH_PROB){
      double sum_mean = 0, sum_var = 0;
      for(int i = 0; i < times; i++){
        auto data = run(assignation,checkoutLambda,chickenProb);
        sum_mean += data.mean;
        sum_var += data.variance;
      }
      return {sum_mean / times, sum_var / times};
    }

    void stats(vector<int> asig, int time=NUMBER_CYCLES, double checkoutLambda = CHECKOUT_LAMBDA) {
      vector<double> allTimes, mean, var, median,minimum,maximum,mode;
      map<string,vector<double>> coviarance;
      for (int i = 0; i < time; i++) {
        auto data = run(asig,checkoutLambda,FOURTH_PROB);
        allTimes.insert(allTimes.end(),data.time.begin(),data.time.end());
        mean.push_back(data.mean);
        var.push_back(data.variance);
        median.push_back(data.median);
        minimum.push_back(data.minimum);
        maximum.push_back(data.maximum);
        mode.push_back(data.mode);
        for (auto const& [name, val] : data.stationTimes) {
          coviarance[name].push_back(val);
        }
      }
      sort(allTimes.begin(), allTimes.end());
      int n=allTimes.size();
      vector<double> perc, quar;
      { // Quartiles
        for (int k=1; k<=3; k++) {
          int pos=(k*(n+1))/4;
          assert(pos>0);
          double dif=k*(n+1)/4.0-pos;
          if ((k*(n+1))%4==0) quar.push_back(allTimes[pos-1]);
          else quar.push_back(allTimes[pos-1]+dif*(allTimes[pos]-allTimes[pos-1]));
        }
      }
      { // Percentiles
        for (int i = 1; i < 100; i++) {
          perc.push_back(percentil(allTimes,i));
        }
      }
      vector<double> x(time);
      iota(x.begin(), x.end(),1.0);
      string s = to_string(asig[0]) + " - " + to_string(asig[1]) + " - " + to_string(asig[2]) + " - " +
        to_string(asig[3]) + " - " + to_string(asig[4]);
      chat.make(x,mean,"Grafica de Media de : " + s);
      chat.make(x,var,"Grafica de varianza de : " + s);
      chat.make(x,median,"Grafica de Mediana de : " + s);
      chat.make(x,minimum,"Grafica de Minimo de : " + s);
      chat.make(x,maximum,"Grafica de Maximo de : " + s);
      chat.make(x,mode,"Grafica de Moda de : " + s);
      for (auto & [name, vec] : coviarance) {
        chat.make(x,vec,"Grafica de Covarianza de : " + name);
      }
      x.assign(99,0);
      iota(x.begin(),x.end(),1.0);
      chat.make(x,perc,"Grafica de Percentiles de : " + s);
      x.assign(3,0);
      iota(x.begin(),x.end(),1.0);
      chat.make(x,quar,"Grafica de Quartiles de : " + s);

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