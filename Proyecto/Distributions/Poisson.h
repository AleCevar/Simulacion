#ifndef SIMULACION_POISSON_H
#define SIMULACION_POISSON_H

#include "../Header.h"
#include "Distribution.h"
#include "../Tests/ChiSquare.h"
#include "../Tests/KolmogorovSmirnov.h"

class Poisson : public Distribution {
  private:
    double lambda;
    mt19937 gen;
    poisson_distribution<> dist;
    boost::math::poisson func;
    ChiSquare chiSquare;
    KolmogorovSmirnov kolmogorov;

  public:
    explicit Poisson(double lambda_) : lambda(lambda_) {
      random_device rd;
      gen = mt19937(rd());
      dist = poisson_distribution<>(lambda);
      func = boost::math::poisson(lambda);
      chiSquare = ChiSquare();
      kolmogorov = KolmogorovSmirnov();
    }
    
    double generate() override {return dist(gen);}

    bool test() override {
      int total = 1e5;
      map<double,int> data;   
      for(int i=0; i < total; i++) data[generate()]++;
      vector<double> fo, pe;
      for(auto [x,y] : data) {
        fo.push_back(y);
        pe.push_back(pdf(func, x));
      }
      cout << "Poisson Tests - Lambda = " << lambda << '\n';
      int res = 0;
      res |= chiSquare.test(fo,pe);
      res |= kolmogorov.test(fo,pe);
      return res;
    }
};

#endif