#include <bits/stdc++.h>
#include <fstream>
#include <iostream>

using namespace std;

using my_clock = chrono::steady_clock;
struct Random {
	mt19937_64 engine;
	Random(): engine(my_clock::now().time_since_epoch().count()) {}
	template<class Int>Int integer(Int n) {return integer<Int>(0, n);} // `[0,n)`
	template<class Int>Int integer(Int l, Int r)
		{return uniform_int_distribution{l, r-1}(engine);} // `[l,r)`
	double real() {return uniform_real_distribution{}(engine);} // `[0,1)`
} rng;


int main(){
    Random randon;
    ofstream file("Muestras/muestra_c++_int.txt");
    for(int i = 0; i < 1e6; i++){
        file << to_string(randon.integer(9)+1) << '\n';
    }
    return 0;
}