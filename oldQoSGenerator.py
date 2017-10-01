#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:04:53 2017

@author: nithilaksh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 20 01:26:32 2017

@author: nithilaksh
"""

#QoS Generator and Storing
#use itertools.product(listof lists)
from NetworkReader import *
from oldPresolver import *
import itertools

#D = nI*[0]
#B = nI*[0]

#B = [[1,0],[3,4,5],[5,6,7]]

QoSdict = {}
listOlists = []
for i in range(0,nI):
    listOlists.append(np.arange(0,Dmax[i]+1))

for i in range(0,nI):
    listOlists.append(np.arange(0,Dmax[i]+1,0.5))

totalIters = 1

for i in range(0,2*nI):
    totalIters = totalIters * len(listOlists[i])

for i in range(1,totalIters+1):
    dummy =[]
    for j in range(0, len(listOlists)):
        k = int(np.floor((i%((j+1)*len(listOlists[j])))/(j+1)))
        dummy.append(listOlists[j][k])
    QoS1,QoS2 = IPPresolver(nI,nJ,nL,R,dummy[0:nI],C,dummy[nI:2*nI],a)
    dummyDict = {tuple(dummy) : [QoS1,QoS2]}
    print(i)
    QoSdict.update(dummyDict)


'''    
bidDemandCombs = list(itertools.product(*listOlists))

for i in range(0, len(bidDemandCombs)):
    QoS1,QoS2 = IPPresolver(nI,nJ,nL,R,bidDemandCombs[i][0:nI],C,bidDemandCombs[i][nI:2*nI],a)
    dummyDict = {tuple(bidDemandCombs[i]) : [QoS1,QoS2]}
    QoSdict.update(dummyDict)
'''
#print(QoSdict)

    #print (B[0][i%2],B[1][int(np.floor((i%6)/2))],B[2][int(np.floor((i%9)/3))])