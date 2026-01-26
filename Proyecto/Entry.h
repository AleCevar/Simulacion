#ifndef SIMULACION_ENTRY_H
#define SIMULACION_ENTRY_H

#include "Distributions/Distribution.h"
#include "Servers/Checkout.h"
#include "Servers/Station.h"

using namespace std;

class Entry {
  private:
    Distribution * arriveDis;
    Distribution * amountDis;
    int numServers;
    const int limitTime = LIMIT_TIME;
    vector<Station> stations;
    vector<Checkout> servers;
    vector<Client*> clients;

  int findNextServer(){
    int pos=0;
    for (int i = 0; i < numServers; i++) {
      if(servers[i].getLastTime()<servers[pos].getLastTime())
        pos=i;
    }
    return pos;
  }

  public:
    Entry(Distribution * arriveDis_, Distribution * amountDis_, Distribution * checkoutDis_, vector<Station> &stations_, int numServers_) : amountDis(amountDis_), arriveDis(arriveDis_), numServers(numServers_) , stations(stations_){
      servers.resize(numServers);
      for (int i = 0; i < numServers; i++) {
        servers[i] = Checkout(checkoutDis_, i);
      }
    }

    void start(){
      double currentTime = arriveDis->generate();
      int id=0;
      while(currentTime <= limitTime) {
        show("Client "<<id<<" arrives at start: "<<currentTime);
        Client * newc =new Client(id, currentTime);
        clients.push_back(newc);
        int pos = findNextServer();  
        servers[pos].attendClient(newc);
        for(auto &s : stations){
          if(s.wantToBuy()){
            int amount = amountDis->generate();
            show("Client "<<id<<" buys "<<amount<<" "<<s.getName());
            while((amount--)>0) s.addOrder(newc);
          }
        }
        id++;
        currentTime += arriveDis->generate();
      }
      for(auto &s : stations) s.start();
    #ifdef SHOW 
      resume();
    #endif
    }

    void resume() {
      cout<<"Client ID,Arrival time,Checkout exit,Exit time,Total time\n";
      for(auto e: clients) 
      cout<<e->getId()<<','<<e->getArrivalTime()<<','
      <<e->getCheckoutExitTime()<<','<<e->getExitTime()<<','<<e->getTotalTime()<<'\n';
    }

    pair<double,double> getEstadistics(){
      double sum = 0;
      for(auto client : clients) sum += client->getTotalTime();
      double mean = sum / int(clients.size());
      double variance = 0;
      for(auto e: clients) variance+=pow(mean-e->getTotalTime(), 2);
      variance/=int(clients.size());
      return {mean,variance};
    }

    Statistic getAllStats(){
      double sum = 0;
      Statistic data;
      for(auto client : clients) {
        sum += client->getTotalTime();
        data.time.push_back(client->getTotalTime());
      }
      int n = (int) data.time.size();
      { // Mean and variance
        double mean = sum / n;
        double variance = 0;
        for(auto e: clients) variance+=pow(mean-e->getTotalTime(), 2);
        variance/=n;
        data.mean=mean;
        data.variance=variance;
      }
      { // median
        if(n%2) data.median = data.time[n/2];
        else data.median = (data.time[n/2-1] + data.time[n/2])/2;
      }
      { //Mode
        map<int,int> cnt;
        for(auto e: data.time) cnt[int(e)]++;
        pair<int, int> mode={0, 0};
        for (auto [x,y] : cnt) mode = max(mode,{y,x});
        data.mode = mode.second;
      }
      { // Min _ Max
        data.minimum = *min_element(data.time.begin(), data.time.end());
        data.maximum = *max_element(data.time.begin(), data.time.end());
      }
      { // Covariance
        for (int i = 0; i < 5; i++) {
          for (int j = i+1; j < 5; j++) {
            double mux = 0, muy=0;
            for (auto const & c : clients) {
              mux += c->getWaitTime(names[i]);
              muy += c->getWaitTime(names[j]);
            }
            mux /= n;
            muy /= n;
            sum = 0;
            for (auto const & c : clients) {
               sum += (c->getWaitTime(names[i]) - mux) * (c->getWaitTime(names[j]) - muy);
            }
            data.stationTimes[names[i]+"-"+names[j]] = sum/n;
          }
        }
      }
      return data;
    }
};

#endif