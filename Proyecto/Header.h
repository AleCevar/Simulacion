#ifndef SIMULACION_HEADER_H
#define SIMULACION_HEADER_H

#include <iostream>
#include <vector>
#include <random>
#include <algorithm>
#include <map>

#include <boost/math/distributions/chi_squared.hpp>
#include <boost/math/distributions/poisson.hpp>
#include <boost/math/distributions/binomial.hpp>
#include <boost/math/distributions/geometric.hpp>
#include <boost/math/distributions/normal.hpp>
#include <boost/math/distributions/exponential.hpp>


using namespace std;

#ifdef LOCAL
#define show(ARG) cout<<ARG<<endl
#define debug(ARG) cout<<"["<<#ARG<<"]: "<<ARG<<endl
#else
#define show(ARG) 42
#define debug(ARG) 42
#endif

#define EXTRA_PEOPLE 7
#define LIMIT_TIME 480
#define NUMBER_CYCLES 100

#define DRI_LAMBDA 1/0.75
#define FRY_MEAN 3
#define FRY_DESVIATION 1
#define DES_N 5
#define DES_P 0.6
#define CHI_P 0.1
#define CHECKOUT_LAMBDA 1/2.5
#define AMOUNT_N 5
#define AMOUNT_P 2.0/5
#define ARRIVE_LAMBDA 3
#define FIRST_PROB 0.9
#define SECOND_PROB 0.7
#define THIRD_PROB 0.25
#define FOURTH_PROB 0.3
#define FIRST_NAME "Drinks"
#define SECOND_NAME "Fryer"
#define THIRD_NAME "Desserts"
#define FOURTH_NAME "Chicken"

#define NUMBER_DECIMALS 100.0

#endif