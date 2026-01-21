#ifndef SIMULACION_CHARTMAKER_H
#define SIMULACION_CHARTMAKER_H

#include "Header.h"

class ChartMaker {
  private:
    FILE* gnuplot;
    int n; 

  public:
    ChartMaker() : n(1) {
      gnuplot = popen("gnuplot -persistent", "w");
    }

    ~ChartMaker(){
      pclose(gnuplot);
    }

    void make(vector<double> & x, vector<double> & y, string title){
      assert((int)x.size() == (int)y.size());
      fprintf(gnuplot, "set term qt %d\n", n++);
      fprintf(gnuplot, "set title '%s'\n", title.c_str());
      fprintf(gnuplot, "set xlabel 'x'\n");
      fprintf(gnuplot, "set ylabel 'y'\n");
      fprintf(gnuplot, "plot '-' with lines\n");
      for(int i = 0; i < (int)x.size(); i++)
        fprintf(gnuplot, "%lf %lf\n", x[i], y[i]);
      fprintf(gnuplot, "e\n");
      fflush(gnuplot);
    }
};

#endif