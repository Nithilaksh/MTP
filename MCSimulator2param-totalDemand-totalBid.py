#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:36:53 2017

@author: nithilaksh
"""

from presolver import *
from QoSGenerrator import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D



    
#IPPresolver(nI,nJ,nL,R,D,C,B,a)
maxRep =1000
refinement = 0.01
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
MElambda =[]
MEQoS = []
maxDemand = max(Dmax)

for Ed in np.arange(0, maxDemand, refinement):
    alph = 1 - (2*Ed)/(maxDemand+1)
    upBoundEb= (1-alph)*(Ed+nI*epsilon)
    lowBoundEb= (1-alph)*(Ed-nI* tepsilon)
    for Eb in np.arange(lowBoundEb, upBoundEb, refinement):
        for n in range(0,maxRep):
            for i in range(0,nI):    
                rand = random.uniform(0,1)
                if rand <= alph:
                    B[i] = 0
                    D[i] = 0
                else:
                    D[i] = np.random.randint(1,Dmax[i]+1)
            #rand2 = np.random.randint(0,2)
                    p = 0.5*((Eb/(1-alph))-Ed + 1)
                    rand2 = random.uniform(0,1)
                    if rand2 <= p:
                        B[i] = D[i] + epsilon
                    else:
                        B[i] = D[i] - epsilon
        #QoS1, QoS2 = IPPresolver(nI,nJ,nL,R,D,C,B,a)
            (QoS1, QoS2) = QoSdict[tuple(D+B)]
            EQoS1 += QoS1
            EQoS2 += QoS2
        EQoS1 = EQoS1/maxRep
        EQoS2 = EQoS2/maxRep
        MElambda.append([Ed,Eb])
        MEQoS.append([EQoS1,EQoS2])
        print([Ed,Eb], [EQoS1, EQoS2])

lambdaArray = np.array(MElambda)
QoSArray = np.array(MEQoS)

plt.figure(figsize=(10,10))
plt.xticks(np.arange(0,3.2,0.2))
plt.yticks(np.arange(0,3.2,0.2))
plt.xlabel("Expexted Demand, lambda1", fontsize = 16)
plt.ylabel("Expected QoS1", fontsize = 16)
plt.ylim(0, 2.2)
plt.xlim(0, 3)
plt.plot(lambdaArray[:,0], QoSArray[:,0], color = "blue", label = "QoS1 v/s lambda1")
plt.scatter(lambdaArray[:,1], QoSArray[:,1], color = "green", label = "QoS2 v/s lambda1")
plt.plot(lambdaArray[:,0], lambdaArray[:,0], color = "orange", label = "lambda1 = QoS1 line")
plt.legend(loc = 'upper right')
#plt.plot(len(MEd)*[1.134],MEd)


fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,135)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS2")
ax.scatter(lambdaArray[:,0], lambdaArray[:,1], QoSArray[:,1], s = 0.1)