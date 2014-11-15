#!/usr/bin/python2
# -*- coding: utf-8 -*-

def alpha():
    for i in range(97, 123):
        print chr(i)

def alpha2():
    for i in range(97, 123):
        if i % 2 == 0:
            print chr(i)


def palindrom(s):
    return s == s[::-1]


# alpha()
# alpha2()

# print palindrom("kajak")
# print palindrom("lista")


def filter_alpha(char):
    alphabet = str([chr(x) for x in range(97, 123)])
    return  char in alphabet

print filter(filter_alpha, '821098309łół#$%@#$%(#@*$(*@(#*$*#18abcdefghijk4320543285jfslkf04380943')

def filter_n_length(n):
    return lambda item : len(item) <= n

def filter_long(items, n):
    f = filter_n_length(n)
    print filter(filter_n_length(n), items)


input = ['sj', 'jdsa', 'jdksjdkjsad']
filter_long(input, 2)
filter_long(input, 4)
