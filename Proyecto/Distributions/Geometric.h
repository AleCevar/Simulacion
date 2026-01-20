#ifndef SIMULACION_GEOMETRIC_H
#define SIMULACION_GEOMETRIC_H

#include "../Header.h"
#include "Distribution.h"
#include "../Tests/ChiSquare.h"
#include "../Tests/KolmogorovSmirnov.h"

class Geometric : public Distribution {
  private:
    double p;
    mt19937 gen;
    geometric_distribution<> dist;
    boost::math::geometric func;
    ChiSquare chiSquare;
    KolmogorovSmirnov kolmogorov;

  public:
    explicit Geometric(double p_) : func(p_){
      p = p_;
      random_device rd;
      gen = mt19937(rd());
      dist = geometric_distribution<>(p);
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
      cout << "Geometric Tests - p = " << p << '\n';
      int res = 0;
      res |= chiSquare.test(fo,pe);
      res |= kolmogorov.test(fo,pe);
      return res;
    }

};

#endif