#include "Configurer.h"

void brute(Run & run){
  double mnMean = 1e9, mxMean = 0, mnVar = 1e9, mxVar = 0;
  vector<int> bestMean, worstMean, bestVar, worstVar;
  for(int i = 0; i <= EXTRA_PEOPLE; i++){
    for(int j = 0; j <= EXTRA_PEOPLE - i; j++){
      for(int k = 0; k <= EXTRA_PEOPLE - i -j; k++){
        for(int m = 0; m <= EXTRA_PEOPLE - i - j - k; m++){
        vector<int> asig={1 + i, 1 + j, 1 + k, 
                1 + m, 1 + EXTRA_PEOPLE - i - j - k - m};
          auto[prom, var] = run.simulate(asig, NUMBER_CYCLES);
          if(prom < mnMean){
            mnMean = prom;
            bestMean = asig;
          }
          if(prom > mxMean){
            mxMean = prom;
            worstMean = asig;
          }
          if(var < mnVar){
            mnVar = var;
            bestVar = asig;
          }
          if(var > mxVar){
            mxVar = var;
            worstVar = asig;
          }
        }
      }
    }
  }
  cout << "Best sample average : " << mnMean << '\n';
  cout << "Best configuration: ";
  for(auto x : bestMean) cout << x << ' '; cout << '\n';
  cout << "Worst sample average : " << mxMean << '\n';
  cout << "Worst configuration: ";
  for(auto x : worstMean) cout << x << ' '; cout << '\n';

  cout << "Best sample variance : " << mnVar << '\n';
  cout << "Best configuration: ";
  for(auto x : bestVar) cout << x << ' '; cout << '\n';
  cout << "Worst sample variance : " << mxVar << '\n';
  cout << "Worst configuration: ";
  for(auto x : worstVar) cout << x << ' '; cout << '\n';
}

int main(){
  Run run = Run();
  // brute(run);
  // run.simulate({3,2,2,1,5}, 1);
  run.runTests();
  return 0;
}