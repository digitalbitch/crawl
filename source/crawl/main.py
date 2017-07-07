#!/usr/bin/env python
import argparse

class loader:


    def __init__(self,args=None):
        parser = argparse.ArgumentParser()
        parser.add_argument("-o", "--outputnamebase", dest='filenameportion', help="intermediate and final output files will use this as unique portion of file name")
        parser.add_argument("-p", "--pattern", dest="searchPattern", help="use this pattern")
        parser.add_argument("-r", "--runners", dest="numberRunners", help="number of agents to run")
        parser.add_argument("-d", "--depth",  dest="numberDepth", help="search depth to run to 1-5")

        self.args=parser.parse_args();

    def set_data(self,args):
        self.args = parser.parse_args(args);


    def get_data(self):
        return self.args;
l=loader();
v=l.get_data();
print(vars(v));
