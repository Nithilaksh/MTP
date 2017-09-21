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



    
#IPPresolver(nI,nJ,nL,R,D,C,B,a)
maxRep =100
refinement = 0.05
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
EQoS2 = 0
MEd =[]
MQoS1 = []
MQoS2 = []

for Ed in np.arange(0, max(Dmax), refinement):
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
        QoS1, QoS2 = IPPresolver(nI,nJ,nL,R,D,C,B,a)
        EQoS1 += QoS1
        EQoS2 += QoS2
    EQoS1 = EQoS1/maxRep
    EQoS2 = EQoS2/maxRep
    
    MEd.append(Ed)
    MQoS1.append(EQoS1)
    MQoS2.append(EQoS2)
    print(Ed,EQoS1,EQoS2)

plt.figure(figsize=(10,10))
plt.xticks(np.arange(0,3.2,0.2))
plt.yticks(np.arange(0,3.2,0.2))
plt.xlabel("Expexted Demand, lambda1", fontsize = 16)
plt.ylabel("Expected QoS1", fontsize = 16)
plt.ylim(0, 2.2)
plt.xlim(0, 3)
plt.legend(loc = 'upper right')
plt.plot(MEd, MQoS1, color = "blue", label = "QoS1 v/s lambda1")
plt.plot(MEd, MQoS2, color = "green", label = "QoS1 v/s lambda1")
plt.plot(MEd, MEd, color = "orange", label = "lambda1 = QoS1 line")
plt.plot(len(MEd)*[1.134],MEd)

#for i  in range(0,len(MEd)):
 #   print(MEd[i],MQ[i])