#!/usr/bin/python2
# -*- coding: utf-8 -*-

import pdb

def squares():
    x = 1
    while True:
        yield x
        yield x**2
        x = x + 1


sq = squares()
pdb.set_trace()

for x in range(100):
    print "number: %s" % sq.next()
    print "square: %s" % sq.next()
