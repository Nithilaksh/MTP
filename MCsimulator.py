#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:05:09 2017

@author: nithilaksh
"""

from NetworkReader import *
from presolver import *
import random
import matplotlib.pyplot as plt


#Bid Range Matrix
#Bmax=[] 

#for i in range(0,nI):
   # Bmax.append(float(input("Max Bid of customer " + str(i) + " ")))

#Bmax = [6,5,5]
    
#Initial Demand Matrix

Dmax=[]

for i in range(0,nI):
    Dmax.append(float(input("Initial Demand of Customer " + str(i) + " ")))
    
#IPPresolver(nI,nJ,nL,R,D,C,B,a)
maxRep =1000
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
EQoS1 = 0
MEd =[]
MQ = []

for Ed in np.arange(0, 3, 0.01):
    for n in range(0,maxRep):
        for i in range(0,nI):
            alph = 1 - (2*Ed)/(Dmax[i]+1)
        
            rand = random.uniform(0,1)
            if rand <= alph:
                B[i] = 0
                D[i] = 0
            else:
                D[i] = np.random.randint(1,Dmax[i]+1)
                #rand2 = np.random.randint(0,2)
                upBoundEb= (1-alph)*(Ed+epsilon)
                lowBoundEb= (1-alph)*(Ed-epsilon)
                for Eb in np.arange(lowBoundEb, upBoundEb, 0.01):
                    p = 0.5*((Eb/(1-alph))-Ed + 1)
                    rand2 = random.uniform(0,1)
                    if rand2 <= p:
                        B[i] = D[i] + epsilon
                    else:
                        B[i] = D[i] - epsilon
        QoS1 = IPPresolver(nI,nJ,nL,R,D,C,B,a)
        EQoS1 += QoS1
    EQoS1 = EQoS1/maxRep
    
    MEd.append(Ed)
    MQ.append(EQoS1)
    print(Ed,EQoS1)

    
plt.plot(MEd, MQ, MEd, MEd)