#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:08:56 2017

@author: nithilaksh
"""

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

    #for i in range(0,nI):
        #print(value(x[i]))
    QoS1=0.0
    
    for i in range(0,nI):
        if D[i] != 0:
            QoS1 = QoS1 + 1 - (value(x[i])/D[i])
        else:
            QoS1 = QoS1 + 1
            #print(type(value(x[i])))
    
    #List of customers on links
    custLinkList = []
    
    for l in range(0,nL):
        custLinkList.append([])
        for i in range(0,nI):
            if l in R[i]:
                custLinkList[l].append(i)
    
    strikePriceList = [] #For each link
    
    for l in range(0,nL):      
        strikePriceList.append(0)
        for j in range(0,nJ):
            if value(y[j][l]) > 0:
                if strikePriceList[l] < a[j][l]:
                    strikePriceList[l] = a[j][l]
            
    maxChargePrice = []#For each link
    
    for l in range(0,nL):
        maxChargePrice.append(0)
        for i in custLinkList[l]:
            if value(x[i]) > maxChargePrice[l]:
                maxChargePrice[l] = B[i]
    
    custMaxPrice =[]
    for i in range(0,nI):
        custMaxPrice.append(0)
        custMaxPrice[i] = max([maxChargePrice[l]  for l in R[i]])
    
    custTotalPrice =[]
    for i in range(0,nI):
        custTotalPrice.append(0)
        for l in R[i]:
            custTotalPrice[i] += strikePriceList[l]
    
    QoS2 = 0.0
    for i in range(0,nI):
        if custMaxPrice[i] != 0:
            QoS2 = QoS2 + (1 - (custTotalPrice[i]/custMaxPrice[i]))
        else:
            QoS2 = QoS2 + 1
            
    return QoS1, QoS2