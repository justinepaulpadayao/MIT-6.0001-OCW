# -*- coding: utf-8 -*-
"""
Created on Sun Oct  9 11:27:54 2016

@author: ericgrimson
"""

def linear_search(L, e):
    return any(e == L[i] for i in range(len(L)))

testList = [1, 3, 4, 5, 9, 18, 27]

def search(L, e):
    for i in range(len(L)):
        if L[i] == e:
            return True
        if L[i] > e:
            return False
    return False


def isSubset(L1, L2):
    for e1 in L1:
        matched = any(e1 == e2 for e2 in L2)
        if not matched:
            return False
    return True


testSet = [1, 2, 3, 4, 5]
testSet1 = [1, 5, 3]
testSet2 = [1, 6]

def intersect(L1, L2):
    tmp = []
    for e1 in L1:
        tmp.extend(e1 for e2 in L2 if e1 == e2)
    res = []
    for e in tmp:
        if e not in res:
            res.append(e)
    return res
