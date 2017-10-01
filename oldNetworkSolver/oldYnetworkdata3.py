#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:11:34 2017

@author: nithilaksh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:10:29 2017

@author: nithilaksh
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 23 05:06:47 2017

@author: nithilaksh
"""

import pickle
from oldNetworkReader import *
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

itersDiv = totalIters/4

for i in range(int(2*itersDiv)+1, int(3*itersDiv)+1):
    dummy =[]
    for j in range(0, len(listOlists)):
        k = int(np.floor((i%((j+1)*len(listOlists[j])))/(j+1)))
        dummy.append(listOlists[j][k])
    QoS1,QoS2 = IPPresolver(nI,nJ,nL,R,dummy[0:nI],C,dummy[nI:2*nI],a)
    dummyDict = {tuple(dummy) : [QoS1,QoS2]}
   # if i%1000 == 0:
    #    print(i)
    QoSdict.update(dummyDict)

output = open("oldY_data3.pkl", 'wb')
pickle.dump(QoSdict, output)
output.close()