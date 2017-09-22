#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 00:07:56 2017

@author: nithilaksh
"""

import math
import numpy as np
from pulp import *

#Read Inputs

file = open("InputTemplate.txt", "r")
file.readline()
file.readline()

#Number of cutomers
nI = int(file.readline())
file.readline()

#Number of links
nL = int(file.readline())
file.readline()

#Number of firms
nJ = int(file.readline())
file.readline()

#Route matrix
R = [] 
for i in range(0,nI):
    R.append([])
    line = file.readline()
    data = line.split()
    for j in range(0, len(data)):
        R[i].append(float(data[j]))

file.readline()

#Demand matrix
D = []
for i in range(0,nI):
    D.append(float(file.readline()))

file.readline()
file.readline()

#Capacity Matrix
C = []
for i in range(0,nJ):
    C.append([])
    line = file.readline()
    data = line.split()
    for j in range(0, len(data)):
        C[i].append(float(data[j]))

file.readline()
        
#Bid matrix
B=[]
for i in range(0,nI):
    B.append(float(file.readline()))

file.readline()

#Firm link cost matrix
a = []
for i in range(0,nJ):
    a.append([])
    line = file.readline()
    data = line.split()
    for j in range(0,len(data)):
        a[i].append(float(data[j]))

############################################################################################

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


