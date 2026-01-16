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
    const int limitTime = 480; //480
    vector<Station> stations;
    vector<Checkout> servers;
    vector<Client> clients;

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
        show("Client Arrival at start: "<<id<<' '<<currentTime);
        clients.push_back(Client(id, currentTime));
        int pos = findNextServer();  
        servers[pos].attendClient(&clients.back());
        for(auto s : stations){
          if(s.wantToBuy()){
            int amount = amountDis->generate();
            show("Client "<<id<<" buys "<<amount<<" "<<s.getName());
            while((amount--)>0) s.addOrder(&clients.back());
          }
        }
        id++;
        currentTime += arriveDis->generate();
      }
      for(auto s : stations) s.start();
    }
};

#endif