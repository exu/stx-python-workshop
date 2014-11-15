#!/usr/bin/python2
# -*- coding: utf-8 -*-

print dir(str)
print callable(str)

class Man:
    legs_count = 10028

man = Man()
print getattr(man, 'legs_count')
print man.legs_count
