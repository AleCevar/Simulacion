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
    uniform_real_distribution<double> random;
    boost::math::normal func;
    ChiSquare chiSquare;
    KolmogorovSmirnov kolmogorov;
    vector<double> chart;

  public:
    explicit Normal(double mean_, double stddev_) : mean(mean_), stddev(stddev_) {
      random_device rd;
      gen = mt19937(rd());
      chiSquare = ChiSquare();
      kolmogorov = KolmogorovSmirnov();
      func = boost::math::normal(mean,stddev);
      double out = boost::math::cdf(func, 0);
      random = uniform_real_distribution<double>(out, boost::math::cdf(func,6));
      for(int i = 1; i <= 6; i++){
        chart.push_back(cdf(func, i) - out);
      }
    }

    double generate() override {
      double num = random(gen);
      int val=0;
      for(int i=0; i<6; i++) if(num<=chart[i]){
        val=i+1;
        break;
      }
      return val;
    } 

    bool test() override {
      int total = 1e5;
      map<double,int> data;   
      for(int i=0; i < total; i++) data[generate()]++;
      vector<double> fo, pe;
      for(auto [x,y] : data) {
        fo.push_back(y);
        pe.push_back(cdf(func, x) - cdf(func, x-1));
      }
      cout << "Normal Tests - mean = " << mean << " deviation = " << stddev << '\n';
      int res = 0;
      res |= chiSquare.test(fo,pe);
      res |= kolmogorov.test(fo,pe);
      return res;
    }

};

#endif