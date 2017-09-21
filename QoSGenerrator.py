#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 01:26:32 2017

@author: nithilaksh
"""

#QoS Generator and Storing
#use itertools.product(listof lists)
from NetworkReader import *
from presolver import *
import itertools

D = nI*[0]
B = nI*[0]

B = [[1,0],[3,4,5],[5,6,7]]

'''
for i in range(1,19):
    dummy =[]
    for j in range(0, len(B)):
        k = int(np.floor((i%((j+1)*len(B[j])))/(j+1)))
        dummy.append(B[j][k])
    print(dummy)
'''

listOlists = []
for i in range(0,nI):
    listOlists.append(np.arange(0,Dmax[i]+1))

for i in range(0,nI):
    listOlists.append(np.arange(0,Dmax[i]+1,0.5))
    
bidDemandCombs = list(itertools.product(*listOlists))

for i in range(0, len(bidDemandCombs)):
    QoS1,QoS2 = IPPresolver(nI,nJ,nL,R,bidDemandCombs[i][0:nI],C,bidDemandCombs[i][nI:2*nI],a)

print(QoS1,QoS2)

    #print (B[0][i%2],B[1][int(np.floor((i%6)/2))],B[2][int(np.floor((i%9)/3))])