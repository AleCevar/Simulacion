#ifndef SIMULACION_SERVER_H
#define SIMULACION_SERVER_H

#include "../Distributions/Distribution.h"
#include "../Client/Client.h"

using namespace std;

class Server {
  private:
    Distribution * dis;
    double lastTime;
    int id;

  public:
    Server(){}

    Server(Distribution * dis_, int id_) : dis(dis_), lastTime(0), id(id_) {}

    double getTime(){return dis->generate();}

    double getLastTime() {return lastTime;}
    
    void updateLastTime(double lastTime_){
      lastTime = lastTime_;
    }

    void attendClient(Client* client, string & name){
      double time = getTime();
      double enterTime = max(client->getCheckoutExitTime(), lastTime);
      updateLastTime(time + enterTime);
      client->updateExitTime(time + enterTime, name);
      show("Client "<<client->getId()<<" attended at time "<<enterTime<<" and leaves at "<<lastTime);
    }
};

#endif 