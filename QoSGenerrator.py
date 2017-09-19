#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 01:26:32 2017

@author: nithilaksh
"""

#QoS Generator and Storing
from NetworkReader import *

D = nI*[0]
B = nI*[0]

Dmax=[]

#for i in range(0,nI):
 #   Dmax.append(float(input("Initial Demand of Customer " + str(i) + " ")))

Dmax = [1,1]

for i in range(0,nI):
    for j in range(0,int(Dmax[i]+1)):
        D[i] = j
        #B = nI*[0]
        for k in range(0, nI): 
            
            for l in np.arange(0,Dmax[i]+1):
                B[k] = l
                #print(D,B)
            B[k] = 0

B = nI*[0]

for i in range(0,2):
    for j in range(0,2):
        for k in range(0,2):
            B[j] = k
            print(B)
        B[j] = 0
    #
    #B[i] = 0
