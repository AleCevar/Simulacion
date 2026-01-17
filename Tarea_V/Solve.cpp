#include "Configurer.h"

int main(){
  double mn = 1e9, mx = 0;
  Run run = Run();
  vector<int> best, worst;
  for(int i = 0; i <= 7; i++){
    for(int j = 0; j <= 7 - i; j++){
      for(int k = 0; k <= 7 - i -j; k++){
        for(int m = 0; m <= 7 - i - j - k; m++){
          double prom = run.simulate({
                        1 + i, 
                        1 + j, 
                        1 + k, 
                        1 + m, 
                        1 + 7 - i - j - k - m
                      });
          if(prom < mn){
            mn = prom;
            best = {1 + i, 1 + j, 1 + k, 1 + m, 1 + 7 - i - j - k - m};
          }
          if(prom > mx){
            mx = prom;
            worst = {1 + i, 1 + j, 1 + k, 1 + m, 1 + 7 - i - j - k - m};
          }
        }
      }
    }
  }
  // run.simulate({3,2,2,1,5})
  cout << "Best sample average : " << mn << '\n';
  cout << "Best configuration: ";
  for(auto x : best) cout << x << ' '; cout << '\n';
  cout << "Worst sample average : " << mx << '\n';
  cout << "Worst configuration: ";
  for(auto x : worst) cout << x << ' '; cout << '\n';
  return 0;
}