#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:05:09 2017

@author: nithilaksh
"""

from NetworkReader import *
from presolver import *

#Bid Range Matrix
B=[] 

for i in range(0,nI):
    B.append([])
    B[i].append(float(input("Min Bid of customer " + str(i) + " ")))
    B[i].append(float(input("Max Bid of customer " + str(i) + " ")))

B = [6,5,5]
    
#Initial Demand Matrix

D=[]

for i in range(0,nI):
    D.append(float(input("Initial Demand of Customer " + str(i) + " ")))
    
IPPresolver(nI,nJ,nL,R,D,C,B,a)
