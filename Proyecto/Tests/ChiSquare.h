#ifndef SIMULACION_CHISQUARE_H
#define SIMULACION_CHISQUARE_H

#include "../Header.h"

class ChiSquare {
  private:
    void fix(vector<double> &fe, vector<double> &fo, int m) {
      vector<double> afo={0}, afe={0};
      for(int i=m-1; i>=0; i--) {
        if(fe[i]<5 || afe.back()<5) afe.back()+=fe[i], afo.back()+=fo[i];
        else afe.push_back(fe[i]), afo.push_back(fo[i]);       
      }
      reverse(afe.begin(), afe.end());
      reverse(afo.begin(), afo.end());
      fe=afe;
      fo=afo;
      // está bien? yo sí y usted? 
    }
  public: 
    ChiSquare(){}

    bool test(vector<double> fo, vector<double> pe){
      int n = accumulate(fo.begin(), fo.end(), 0);
      vector<double> fe;
      for(auto x : pe) fe.push_back(x * n);
      fix(fe,fo,(int)fe.size());
      int m = (int) fe.size();
      double obs = 0;
      for(int i = 0; i < m; i++) obs += pow(fe[i] - fo[i], 2) / fe[i];
      boost::math::chi_squared dist(m-1);
      double cri = boost::math::quantile(dist,0.95);
      cout << "Chi Square: ";
      if(obs < cri) cout << "Se tolera: ";
      else cout<< "NO se tolera: ";
      cout << obs << " < " << cri << '\n';
      return obs < cri;
    }
};
#endif