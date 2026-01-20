#ifndef SIMULACION_NORMAL_H
#define SIMULACION_NORMAL_H

#include "../Header.h"
#include "Distribution.h"
#include "../Tests/ChiSquare.h"
#include "../Tests/KolmogorovSmirnov.h"

class Normal : public Distribution {
  private:
    double mean;
    double stddev;
    mt19937 gen;
    normal_distribution<> dist;
    boost::math::normal func;
    ChiSquare chiSquare;
    KolmogorovSmirnov kolmogorov;

  public:
    explicit Normal(double mean_, double stddev_) : mean(mean_), stddev(stddev_) {
      random_device rd;
      gen = mt19937(rd());
      dist = normal_distribution<>(mean,stddev);
      chiSquare = ChiSquare();
      kolmogorov = KolmogorovSmirnov();
      func = boost::math::normal(mean,stddev);
    }

    double generate() override {
      int re = ceil(dist(gen)+1);
      assert(re>=0);
      return re;
    } 
    // ojo negativos >:)

    bool test() override {
      int total = 1e5;
      map<double,int> data;   
      for(int i=0; i < total; i++) data[generate()]++;
      vector<double> fo, pe;
      for(auto [x,y] : data) {
        fo.push_back(y);
        pe.push_back(cdf(func, x+1) - cdf(func, x));
      }
      cout << "Normal Tests - mean = " << mean << "deviation = " << stddev << '\n';
      int res = 0;
      res |= chiSquare.test(fo,pe);
      res |= kolmogorov.test(fo,pe);
      return res;
    }

};

#endif