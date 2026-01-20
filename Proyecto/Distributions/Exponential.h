#ifndef SIMULACION_EXPONENTIAL_H
#define SIMULACION_EXPONENTIAL_H

#include "../Header.h"
#include "Distribution.h"
#include "../Tests/ChiSquare.h"
#include "../Tests/KolmogorovSmirnov.h"

using namespace std;

class Exponential : public Distribution{
private:
    double lambda;
    exponential_distribution<> dist;
    mt19937 gen;
    ChiSquare chiSquare;
    KolmogorovSmirnov kolmogorov;
    boost::math::exponential func;

public:
    explicit Exponential(double media) : lambda(media) {
        random_device rd;
        gen = mt19937(rd());
        dist = exponential_distribution<>(lambda);
        chiSquare = ChiSquare();
        kolmogorov = KolmogorovSmirnov();
        func = boost::math::exponential(lambda);
    }

    double generate() override {return dist(gen);}

    bool test() override {
        int total = 1e5;
        map<double,int> data;   
        for(int i=0; i < total; i++) {
            double x = generate();
            data[trunc(x*NUMBER_DECIMALS) / NUMBER_DECIMALS]++;
        }
        vector<double> fo, pe;
        for(auto [x,y] : data) {
            fo.push_back(y);
            pe.push_back(cdf(func, x + (1/NUMBER_DECIMALS))
                - cdf(func, x));
        }
        cout << "Exponential Tests - lambda = " << lambda << '\n';
        int res = 0;
        res |= chiSquare.test(fo,pe);
        res |= kolmogorov.test(fo,pe);
        return res;
    }

};

#endif 