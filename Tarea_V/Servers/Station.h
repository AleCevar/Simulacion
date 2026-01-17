#ifndef SIMULACION_ESTACION_H
#define SIMULACION_ESTACION_H

#include "../Header.h"
#include "Server.h"
#include "../Client/Client.h"

using namespace std;

class Station {
  private:
    string name;
	  int numServers;
		vector<Server> servers;
    vector<Client*> orders;
    double probBuy;
    mt19937 gen;
    uniform_real_distribution<double> random;

    static bool compare(Client *a, Client *b) {
      return a->getCheckoutExitTime() < b->getCheckoutExitTime();	
    }
		
		int findNextServer() {
			int posit=0;
			for (int i = 0; i < numServers; i++) {
				if(servers[i].getLastTime()<servers[posit].getLastTime())
					posit=i;
			}
			return posit;
		}

  public:
	  Station(string name_, int numServers_, Distribution * dis, double probBuy_) : numServers(numServers_), name(name_) , probBuy(probBuy_) {
			servers.resize(numServers);
      for(int i = 0; i < numServers; i++){
        servers[i] = Server(dis,i);
      }
      random_device rd;
      gen = mt19937(rd());
      random = uniform_real_distribution<double>(0.0, 1.0);
		}
		
    void addOrder(Client * client){
      orders.push_back(client);
    }
    
    bool wantToBuy() {
      double n = random(gen);
      return n < probBuy;
    }
		
		void start(){
      sort(orders.rbegin(), orders.rend(), compare);
			while(!orders.empty()){
        auto client = orders.back(); orders.pop_back();
        int serverId = findNextServer();
        show("Client "<<client->getId()<<" at "<<name<<" on server "<<serverId<<" :");
        servers[serverId].attendClient(client);
      }
    }

    string getName(){
      return name;
    }
};

#endif 