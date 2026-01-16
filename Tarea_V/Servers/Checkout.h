#ifndef SIMULACION_CHECKOUT_H
#define SIMULACION_CHECKOUT_H

#include "../Header.h"
#include "../Distributions/Distribution.h"
#include "../Client/Client.h"

class Checkout {
  private:
    double lastTime;
    Distribution * dis;
    int id;

  public:
    Checkout(){}

    Checkout(Distribution * dis_, int id_) : lastTime(0), dis(dis_), id(id_) {}
    
    double getTime(){return dis->generate();}

    double getLastTime(){return lastTime;}

    void updateLastTime(double lastTime_){
      lastTime = lastTime_;
    }

    void attendClient(Client * client){
      double time = getTime();
      double enterTime = max(client->getArrivalTime(), lastTime);
      show("Client "<<client->getId()<<" attended on server "<<id<<" at time "<<enterTime);
      client->updateCheckoutEnterTime(enterTime);
      client->updateCheckoutExitTime(time + enterTime);
      lastTime=enterTime+time;
      show("Server "<<id<<" free at time "<<lastTime);
    }
};

#endif