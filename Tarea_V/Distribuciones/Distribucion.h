#ifndef SIMULACION_DISTRIBUCION_H
#define SIMULACION_DISTRIBUCION_H

class Distribucion{
  public:
    virtual ~Distribucion() = default;
    virtual double generar() = 0;
};

#endif SIMULACION_DISTRIBUCION_H