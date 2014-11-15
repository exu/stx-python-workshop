#!/usr/bin/python2
# -*- coding: utf-8 -*-

data = range(1, 51)
lc = [x**2 for x in data]
lm = map(lambda x: x**2, data)
print lm == lc

print map(lambda x,y,z:(y,x,z), [1,2,3], [4,5,6], [7,8,9])
