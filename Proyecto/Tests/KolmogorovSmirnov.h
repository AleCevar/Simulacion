#ifndef SIMULACION_KOLMOGOROVSMIRNOV_H
#define SIMULACION_KOLMOGOROVSMIRNOV_H

#include "../Header.h"

class KolmogorovSmirnov {
  public:
    KolmogorovSmirnov(){}

    bool test(vector<double> fo, vector<double> pe){
      vector<double> pea=pe;
      int m=fo.size();
      int n=accumulate(fo.begin(), fo.end(), 0);
      for(int i=1; i<m; i++) pea[i]+=pea[i-1];
      vector<double> foa=fo;
      for(int i=1; i<m; i++) foa[i]+=foa[i-1];
      double obs=0;
      for(int i=0; i<m; i++) obs=max(obs, abs(foa[i]/n-pea[i]));
      double cri = 1.36 / sqrt(n*1.0);
      cout << "Kolmogorov-Smirnov: ";
      if(obs < cri) cout << "Se tolera: ";
      else cout<< "NO se tolera: ";
      cout << obs << " < " << cri << '\n';
      return obs < cri;
    }
};

#endif