#ifndef SIMULACION_ENTRY_H
#define SIMULACION_ENTRY_H

#include "Servers/Server.h"
#include "Distributions/Distribution.h"
#include "Servers/Checkout.h"
#include "Distributions/Exponential.h"
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
};

#endif