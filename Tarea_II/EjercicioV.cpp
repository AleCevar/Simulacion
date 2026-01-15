#include <bits/stdc++.h>

using namespace std;

const int tam=1e8+1;
bitset<tam> b;

void multi(int a, int m, long long x, vector<int> div){
  b.reset();
  while(1) {
    x=(x*a)%m;
    if(b.test(x)) break;
    b.set(x);
  }
  int cp = m;
  for(auto d : div) cp = (cp - (cp/d));
  if(cp == b.count()){
    cout << "Recorrido completo\n";
  }
  else cout << "Recorrido NO completo\n";
}

int main () {
    cout << "Punto a)\n";
    multi(5,64,7,{2});
    cout << "Punto b)\n";
    multi(11,128,9,{2});
    cout << "Punto c)\n";
    multi(221,1e3,3,{2,5});
    cout << "Punto d)\n";
    multi(203,1e5,17,{2,5});
    cout << "Punto e)\n";
    multi(211,1e8,19,{2,5});
    return 0;
}