#!/bin/sh

g++ -I/usr/local/include -L/usr/local/lib -lboost_system --std=c++11 -g3 echo_server.cc
