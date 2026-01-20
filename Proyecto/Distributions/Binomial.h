#ifndef SIMULACION_BINOMIAL_H
#define SIMULACION_BINOMIAL_H

#include "../Header.h"
#include "Distribution.h"
#include "../Tests/ChiSquare.h"
#include "../Tests/KolmogorovSmirnov.h"

class Binomial : public Distribution {
  private:
    int n;
    double p;
    mt19937 gen;
    binomial_distribution<> dist;
    boost::math::binomial func;
    ChiSquare chiSquare;
    KolmogorovSmirnov kolmogorov;

  public:
    explicit Binomial(int n_, double p_) : n(n_), p(p_) {
      random_device rd;
      gen = mt19937(rd());
      dist = binomial_distribution<>(n,p);
      func = boost::math::binomial(n,p);
      chiSquare = ChiSquare();
      kolmogorov = KolmogorovSmirnov();
    }

    double generate() override {return dist(gen);}

    bool test() override {
      int total = 1e5;
      map<double,int> data;   
      for(int i=0; i < total; i++) data[generate()]++;
      vector<double> fo, pe;
      for(auto [x, y] : data) {
        fo.push_back(y);
        pe.push_back(pdf(func, x));
      }
      cout << "Binomial Tests - n = " << n << " p = "<<p<<'\n';
      int res = 0;
      res |= chiSquare.test(fo,pe);
      res |= kolmogorov.test(fo,pe);
      return res;
    }
};

#endif