
#include "Configurer.h"

int main(){
  Run run = Run();
  // for(int i = 0; i <= 7; i++){
  //   for(int j = 0; j <= 7 - i; j++){
  //     for(int k = 0; k <= 7 - i -j; k++){
  //       for(int m = 0; m <= 7 - i - j - k; m++){
  //         run.simulate({1 + i, 
  //                       1 + j, 
  //                       1 + k, 
  //                       1 + m, 
  //                       1 + 7 - i - j - k - m});
  //       }
  //     }
  //   }
  // }
  run.simulate({3,2,2,1,5});
  return 0;
}