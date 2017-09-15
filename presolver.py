#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:10:35 2017

@author: nithilaksh
"""
#Solves the basic presolving algorithm with the simplest default IP formulation

import math
import numpy as np
from pulp import *

def IPPresolver(nI,nJ,nL,R,D,C,B,a):
    IP = LpProblem("Presolver", LpMaximize)

    x = LpVariable.dicts("x", (range(0,nI)), lowBound = 0, cat = LpInteger)

    y = LpVariable.dicts("y", (range(0,nJ), range(0,nL)), lowBound = 0,cat = LpInteger)

#Objective
    IP += lpSum([B[i]*x[i] for i in range(0,nI)]) - lpSum([[a[j][l]*y[j][l] for j in range(0,nJ)]for l in range(0,nL)])

# Constraints
#Allocation Balance

    for l in range(0,nL):
        linkCustomerSet =[]
        for i in range(0,nI):
            if l in R[i]:
                linkCustomerSet.append(i)
    #print(linkCustomerSet)
        IP += lpSum([x[i] for i in linkCustomerSet]) == lpSum([y[j][l] for j in range(0,nJ)]), ""
    
#Demand limits
    for i in range(0,nI):
        IP += x[i] <= D[i]

#Capacity Limits
    for j in range(0,nJ):
        for l in range(0,nL):
            IP += y[j][l] <= C[j][l]

    IP.solve()

    for i in range(0,nI):
        print(value(x[i]))