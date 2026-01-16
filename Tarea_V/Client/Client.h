#ifndef SIMULACION_CLIENT_H
#define SIMULACION_CLIENT_H

#include "../Header.h"

class Client {
  private:
    double arrivalTime;
    double checkoutEnterTime;
    double checkoutExitTime;
    double exitTime;
    int id;

  public:
    Client(int id_, double arrivalTime_) : arrivalTime(arrivalTime_), checkoutEnterTime(0), checkoutExitTime(0), exitTime(0), id(id_) {}

    double getTotalTime() {
      return exitTime-arrivalTime;
    }

    void updateExitTime(double exitTime_){
      exitTime = max(exitTime, exitTime_);
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

    int getId(){
      return id;
    }

};

#endif 