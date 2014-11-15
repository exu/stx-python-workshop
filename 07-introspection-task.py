#!/usr/bin/python2
# -*- coding: utf-8 -*-

################################################################################

print dir(str)
print callable(str)


class Man:
    """
    class comment
    Attributes:
        legs_count The maximum legs_count
    """

    legs_count = 10028

    def legs(self):
        "method comment"
        return Man.legs_count

man = Man()
print getattr(man, 'legs_count')
print man.legs_count.__doc__

################################################################################

def get_all(obj):
    return [i for i in dir(obj)]

def get_attribs(obj):
    return [i for i in dir(obj) if not callable(getattr(obj, i))]

def get_methods(obj):
    return [(i, getattr(obj, i).__doc__) for i in dir(obj) if callable(getattr(obj, i))]


print get_all(man)
print get_attribs(man)
print get_methods(man)
