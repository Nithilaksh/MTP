#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 23:22:10 2017

@author: nithilaksh
"""

file = open("TussarNetwork.txt", "r")
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