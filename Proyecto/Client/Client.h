#ifndef SIMULACION_CLIENT_H
#define SIMULACION_CLIENT_H

#include "../Header.h"

class Client {
  private:
    double arrivalTime;
    double checkoutEnterTime;
    double checkoutExitTime;
    double exitTime;
    map<string, double> waitTimes;
    int id;

  public:
    Client(int id_, double arrivalTime_) : arrivalTime(arrivalTime_), checkoutEnterTime(0), checkoutExitTime(0), exitTime(0), id(id_) {}

    double getTotalTime() {
      return max(exitTime-arrivalTime, checkoutExitTime-arrivalTime);
    }

    void updateExitTime(double exitTime_, string & name){
      exitTime = max(exitTime, exitTime_);
      auto &it=waitTimes[name];
      it = max(it,exitTime_);
    }

    double getWaitTime(string & name) {
      if (name == "Check") return checkoutExitTime - arrivalTime;
      return waitTimes[name] - checkoutExitTime;
    }

    void updateCheckoutExitTime(double checkoutExitTime_){
      checkoutExitTime = checkoutExitTime_;

    }

    void updateCheckoutEnterTime(double checkoutEnterTime_){
      checkoutEnterTime = checkoutEnterTime_;
    }

    double getCheckoutExitTime(){
      return checkoutExitTime;
    }

    double getArrivalTime(){
      return arrivalTime;
    }

    double getExitTime() {
      return exitTime;
    }

    int getId(){
      return id;
    }

};

#endif 