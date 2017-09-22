#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:22:10 2017

@author: nithilaksh
"""

file = open("NetworkTemplate1.txt", "r")
file.readline()
file.readline()

#Number of cutomers
nI = int(file.readline())
file.readline()

#Number of links
nL = int(file.readline())
file.readline()

#Number of firms
nJ = int(file.readline())
file.readline()

#Route matrix
R = [] 
for i in range(0,nI):
    R.append([])
    line = file.readline()
    data = line.split()
    for j in range(0, len(data)):
        R[i].append(int(data[j]))

file.readline()
file.readline()

#Capacity Matrix
C = []
for i in range(0,nJ):
    C.append([])
    line = file.readline()
    data = line.split()
    for j in range(0, len(data)):
        C[i].append(float(data[j]))

file.readline()

#Firm link cost matrix
a = []
for i in range(0,nJ):
    a.append([])
    line = file.readline()
    data = line.split()
    for j in range(0,len(data)):
        a[i].append(float(data[j]))
        
#Bid Range Matrix
#Bmax=[] 

#for i in range(0,nI):
   # Bmax.append(float(input("Max Bid of customer " + str(i) + " ")))

#Bmax = [6,5,5]
    
#Initial Demand Matrix

Dmax=[20,4,15]

#for i in range(0,nI):
 #   Dmax.append(float(input("Initial Demand of Customer " + str(i) + " ")))
    
    