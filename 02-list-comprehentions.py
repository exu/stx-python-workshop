#!/usr/bin/python2
# -*- coding: utf-8 -*-

print "training"
print [x**2 for x in range(10) if x % 2 == 0]
print [x for x in range(101)]
print [x for x in range(101) if x % 2 == 0]
print [l for l in "jsakfkdskjfhdsfkjhds"]

print "dict comprehetions"
print {k: v for k, v in enumerate("abcdefghijklmnopqrstuwxyz")}

print "uzyj list compr aby uzyskac liste literek"
print [l for l in "abcdefghijklmnopqrstuwxyz"]

print "uzyj dict compr aby uzyskac hasha literka : kod ascii"
print {l: ord(l) for l in "abcdefghijklmnopqrstuwxyz"}

print "lista itemów krótszych od 5"
items = ["a", "bb", "ccc", "dddd", "eeeee", "fffffff", "gggggggg"]
print [l for l in items if len(l) <= 5]
