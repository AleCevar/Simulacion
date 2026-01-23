cmake_minimum_required(VERSION 4.1)
project(Proyecto)

set(CMAKE_CXX_STANDARD 14)

include_directories(.)
include_directories(Client)
include_directories(Distributions)
include_directories(Servers)
include_directories(Tests)

add_executable(Proyecto
        Client/Client.h
        Distributions/Binomial.h
        Distributions/Distribution.h
        Distributions/Exponential.h
        Distributions/Geometric.h
        Distributions/Normal.h
        Distributions/Poisson.h
        Servers/Checkout.h
        Servers/Server.h
        Servers/Station.h
        Tests/ChiSquare.h
        Tests/KolmogorovSmirnov.h
        ChartMaker.h
        Configurer.h
        Entry.h
        Header.h
        Solve.cpp)
