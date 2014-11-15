#!/usr/bin/python2
# -*- coding: utf-8 -*-

import pdb

################################################################################

def days():
    days = ["pon", "wt", "sr", "czw", "pt", "so", "nd"]
    for i in range(70):
        yield days[i%7]

sq = days()
# pdb.set_trace()

# while True:
#     print "day: %s" % sq.next()

a = [i for i in sq if i not in ["so", "nd"]]
print a

################################################################################

def infinite_days():
    days = ["pon", "wt", "sr", "czw", "pt", "so", "nd"]
    i = 5 # today :)
    while True:
        yield days[i%7]
        i += 1

sq = infinite_days()

a = [sq.next() for a in range(10)]
a = filter(lambda y : y not in ["so", "nd"], a)
print a
