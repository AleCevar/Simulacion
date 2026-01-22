#include "Configurer.h"
#include "ChartMaker.h"

void brute(){
  Run run = Run();
  double mnMean = 1e9, mxMean = 0, mnVar = 1e9, mxVar = 0;
  vector<int> bestMean, worstMean, bestVar, worstVar;
  for(int i = 0; i <= EXTRA_PEOPLE; i++){
    for(int j = 0; j <= EXTRA_PEOPLE - i; j++){
      for(int k = 0; k <= EXTRA_PEOPLE - i -j; k++){
        for(int m = 0; m <= EXTRA_PEOPLE - i - j - k; m++){
        vector<int> asig={1 + i, 1 + j, 1 + k, 
                1 + m, 1 + EXTRA_PEOPLE - i - j - k - m};
          
          auto[prom, var] = run.simulate(asig);
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
}

void part1() {
  cout<<"1. Pruebas estadisticas de las distribuciones\n";
  Run run = Run();
  run.runTests();
}

void part2a() {
  Run run = Run();
  cout<<"2. a) No se puede. El tiempo converge a los ocho minutos aproximadamente\n";
  vector<double> x, y;
  vector<int> asig(5);
  ChartMaker chat;
  for(int i=5; i<=50; i+=5){
    for(auto &e: asig) e=i;
    x.push_back(i);
    y.push_back(run.simulate(asig, 100).first);
  }
  chat.make(x, y, "Analisis convergencia");
}

vector<int> cost={500, 750, 200, 0, 100};

int calCost(vector<int> c) {
  int sum=0;
  for(int i=0; i<5; i++) sum+=c[i]*cost[i];
  return sum;
}

void part2bc(int money){
  Run run = Run();
  set<pair<double, vector<int>>> best;
  for(int i = 0; i <= EXTRA_PEOPLE; i++){
    for(int j = 0; j <= EXTRA_PEOPLE - i; j++){
      for(int k = 0; k <= EXTRA_PEOPLE - i -j; k++){
        for(int m = 0; m <= EXTRA_PEOPLE - i - j - k; m++)
          for(int x=0; x <=  EXTRA_PEOPLE - i - j - k - m; x++){
          vector<int> asig={1 + i, 1 + j, 1 + k, 1 + m, 1 + x};
          if(calCost(asig) > money) continue;
          auto[prom, var] = run.simulate(asig);
          best.insert({prom,asig});
          if(best.size()>3) best.erase(prev(best.end()));
        }
      }
    }
  }
  for(auto & [m, a] : best){
    cout << "Mean: " << m << '\n';
    cout << "Cost: " << calCost(a) << '\n';
    cout << "Configuration: ";
    for(auto x : a) cout << x << ' ';
    cout << '\n';
  }
}

void part2d(double lambda, int money = 3000){
  part2bc(money);
  cout<<'\n';
  Run run = Run();
  set<pair<double, vector<int>>> best;
  for(int i = 0; i <= EXTRA_PEOPLE; i++){
    for(int j = 0; j <= EXTRA_PEOPLE - i; j++){
      for(int k = 0; k <= EXTRA_PEOPLE - i -j; k++){
        for(int m = 0; m <= EXTRA_PEOPLE - i - j - k; m++)
          for(int x=0; x <=  EXTRA_PEOPLE - i - j - k - m; x++){
          vector<int> asig={1 + i, 1 + j, 1 + k, 1 + m, 1 + x};
          if(calCost(asig) > money) continue;
          auto[prom, var] = run.simulate(asig,NUMBER_CYCLES,lambda);
          best.insert({prom,asig});
          if(best.size()>3) best.erase(prev(best.end()));
        }
      }
    }
  }
  for(auto & [m, a] : best){
    cout << "Mean: " << m << '\n';
    cout << "Cost: " << calCost(a) << '\n';
    cout << "Configuration: ";
    for(auto x : a) cout << x << ' ';
    cout << '\n';
  }
}

void part2e(double chickenProb){
  Run run = Run();
  cout<<"2. e) No se puede. El tiempo converge a los 10 minutos aproximadamente\n";
  vector<double> x, y;
  vector<int> asig(5);
  ChartMaker chat;
  for(int i=5; i<=50; i+=5){
    for(auto &e: asig) e=i;
    x.push_back(i);
    y.push_back(run.simulate(asig, 100, CHECKOUT_LAMBDA, chickenProb).first);
  }
  chat.make(x, y, "Analisis convergencia");
}

int main(){
  // brute();
  // auto [m,v] = run.simulate({100,100,100,100,100}, 100);
  // cout << m << ' ' << v << '\n';
  // part1();
  // part2a();
  // part2bc(3000);
  // part2d(1/2.0);
  // part2e(0.5); 
  return 0;
}