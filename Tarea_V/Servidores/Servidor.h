#ifndef SIMULACION_SERVIDOR_H
#define SIMULACION_SERVIDOR_H

#include "Tarea_V/Distribuciones/Distribucion.h"

using namespace std;

class Servidor {
  private:
    Distribucion * dis;
    double tiempo_ultimo;
    int id;

  public:
    Servidor(Distribucion * dis_, int id_) : dis(dis_), tiempo_ultimo(0), id(id_) {}

    double obtener_duracion(){return dis->generar();}

    double obtener_tiempo() {return tiempo_ultimo;}
    
    void actualizar_tiempo(double tiempo_ultimo_){
      tiempo_ultimo = tiempo_ultimo_;
    }
};

#endif SIMULACION_SERVIDOR_H