#ifndef SIMULACION_HEADER_H
#define SIMULACION_HEADER_H

#include <iostream>
#include <vector>
#include <random>
#include <algorithm>

using namespace std;

#ifdef LOCAL
#define show(ARG) cout<<ARG<<endl
#define debug(ARG) cout<<"["<<#ARG<<"]: "<<ARG<<endl
#else
#define show(ARG) 42
#define debug(ARG) 42
#endif





#endif