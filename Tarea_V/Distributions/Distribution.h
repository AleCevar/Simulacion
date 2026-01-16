#ifndef SIMULACION_DISTRIBUTION_H
#define SIMULACION_DISTRIBUTION_H

#include "../Header.h"

class Distribution{
  public:
    virtual ~Distribution() = default;
    virtual double generate() = 0;
};

#endif 