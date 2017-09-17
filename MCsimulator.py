#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:05:09 2017

@author: nithilaksh
"""

from NetworkReader import *
from presolver import *
import random



#Bid Range Matrix
Bmax=[] 

for i in range(0,nI):
    Bmax.append(float(input("Max Bid of customer " + str(i) + " ")))

Bmax = [6,5,5]
    
#Initial Demand Matrix

Dmax=[]

for i in range(0,nI):
    Dmax.append(float(input("Initial Demand of Customer " + str(i) + " ")))
    
IPPresolver(nI,nJ,nL,R,D,C,B,a)

#Initialize expected demand as 0
Ed = 0
#Initialize expected bid as 0
Eb = 0
#Create alpha for distribution
alph = 0
epsilon = 0.5
#Bid matrix
B = nI*[0] 
D = nI*[0]

for Ed in arange(0, 6, 0.01):
    for i in range(0,nI):
        alph = 1 - (2*Eb)/(Bmax[i]+1)
        
        rand = random.uniform(0,1)
        if rand <= alph:
            B[i] = 0
            D[i] = 0
        else:
            B[i] = np.random.randint(1,Bmax[i]+1)
            rand2 = np.random.randint(0,2)
            if rand2 == 0:
                D[i] = B[i] - epsilon
            else:
                D[i] = B[i] + epsilon
            
            