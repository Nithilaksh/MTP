#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 00:41:14 2017

@author: nithilaksh
"""

#from presolver import *
from QoSGenerrator import *
import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def MCSim_IndEd_IndEb(nI,QoSdict, maxRep, refinement): #Calculates lambda1 and lambda2 as individual expectations for consumers
    
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
    maxEd = nI*0.5*(maxDemand+1)

    for Ed in np.arange(0, maxEd, refinement):
        alph = 1 - (2*Ed)/(maxDemand+1)
        upBoundEb= (1-alph)*(Ed+epsilon)
        lowBoundEb= (1-alph)*(Ed-epsilon)
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
                        p = 0.5*(1+(1/epsilon)*((Eb/(1-alph))-Ed))
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
            #print([Ed,Eb], [EQoS1, EQoS2])

    lambdaArray = np.array(MElambda)
    QoSArray = np.array(MEQoS)

    return(lambdaArray, QoSArray)

####################################################################################

def MCSim_TotEd_IndEb(nI,QoSdict, maxRep, refinement): #Calculates lambda1 and lambda2 as total and individual expectations for consumers
    
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
    maxEd = nI*0.5*(maxDemand+1)
    
    for Ed in np.arange(0, maxEd, refinement):
        alph = 1 - (2*Ed)/((maxDemand+1)*nI)
        upBoundEb= (1-alph)*(Ed+epsilon)
        lowBoundEb= (1-alph)*(Ed-epsilon)
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
                        p = 0.5*(1+(1/epsilon)*((Eb/(1-alph))-Ed))
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
            #print([Ed,Eb], [EQoS1, EQoS2])

    lambdaArray = np.array(MElambda)
    QoSArray = np.array(MEQoS)

    return(lambdaArray, QoSArray)

##########################################################################################

def MCSim_TotEd_TotEb(nI,QoSdict, maxRep, refinement): #Calculates lambda1 and lambda2 as total expectations for consumers
    
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
    maxEd = nI*0.5*(maxDemand+1)

    for Ed in np.arange(0, maxEd, refinement):
        alph = 1 - (2*Ed)/((maxDemand+1)*nI)
        upBoundEb= (1-alph)*(Ed+(epsilon*nI))
        lowBoundEb= (1-alph)*(Ed-(epsilon*nI))
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
                        p = 0.5*(1+(1/(epsilon*nI))*((Eb/(1-alph))-Ed))
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
            #print([Ed,Eb], [EQoS1, EQoS2])

    lambdaArray = np.array(MElambda)
    QoSArray = np.array(MEQoS)

    return(lambdaArray, QoSArray)

#################################################################################################

"""
Main Program
"""

maxRep =1000
refinement = 0.01

lambda_0, QoS_0 = MCSim_IndEd_IndEb(nI, QoSdict, maxRep, refinement)

lambda_1, QoS_1 = MCSim_TotEd_IndEb(nI, QoSdict, maxRep, refinement)

lambda_2, QoS_2 = MCSim_TotEd_TotEb(nI, QoSdict, maxRep, refinement)

###########################################################################################
"""
Plot Figures
"""
"""
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
"""
##################################################################################################
#QoS1 plots
#Orthogonal views
fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(-90,0)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS1")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,0], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,0], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,0], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,-90)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS1")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,0], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,0], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,0], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,0)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS1")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,0], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,0], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,0], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

#Isometric Views

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(45,45)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS1")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,0], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,0], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,0], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,135)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS1")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,0], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,0], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,0], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

############################################################################################################################
#Plots for QoS2
#Orthogonal Views

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(-90,0)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS2")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,1], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,1], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,1], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,-90)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS2")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,1], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,1], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,1], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,0)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS2")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,1], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,1], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,1], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

#Isometric Views

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(45,45)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS2")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,1], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,1], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,1], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(0,135)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS2")
scatter0 = ax.scatter(lambda_0[:,0], lambda_0[:,1], QoS_0[:,1], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambda_1[:,0], lambda_1[:,1], QoS_1[:,1], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambda_2[:,0], lambda_2[:,1], QoS_2[:,1], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])


###########################################################################################
maxDemand = max(Dmax)
maxEd = nI*0.5*(maxDemand+1)
epsilon = 0.5
QoS =[]
lambd =[]


for Ed in np.arange(0, maxEd, 0.01):
    alph = 1 - (2*Ed)/(maxDemand+1)
    upBoundEb= (1-alph)*(Ed+epsilon)
    lowBoundEb= (1-alph)*(Ed-epsilon)
    for Eb in np.arange(lowBoundEb, upBoundEb, 0.01):
        q1 = 2 - 0.0162*Ed*Ed - 0.1667*Ed + 0.185*Ed*Eb - 0.6667*Eb - 0.037*Eb*Eb
        q2 =   - 0.111*Eb*Eb - 0.1398*Eb*Ed - 0.25*Ed - 0.33*Eb + 2
        lambd.append([Ed,Eb])
        QoS.append([q1,q2])

lambdA0 = np.array(lambd)
QoSA0 = np.array(QoS)

for Ed in np.arange(0, maxEd, 0.01):
    alph = 1 - (2*Ed)/((maxDemand+1)*nI)
    upBoundEb= (1-alph)*(Ed+epsilon)
    lowBoundEb= (1-alph)*(Ed-epsilon)
    for Eb in np.arange(lowBoundEb, upBoundEb, 0.01):
        q1 = 2 - 0.0162*Ed*Ed - 0.1667*Ed + 0.185*Ed*Eb - 0.6667*Eb - 0.037*Eb*Eb
        q2 =   - 0.111*Eb*Eb - 0.1398*Eb*Ed - 0.25*Ed - 0.33*Eb + 2
        lambd.append([Ed,Eb])
        QoS.append([q1,q2])
        
lambdA1 = np.array(lambd)
QoSA1 = np.array(QoS)

for Ed in np.arange(0, maxEd, 0.01):
    alph = 1 - (2*Ed)/((maxDemand+1)*nI)
    upBoundEb= (1-alph)*(Ed+epsilon*nI)
    lowBoundEb= (1-alph)*(Ed-epsilon*nI)
    for Eb in np.arange(lowBoundEb, upBoundEb, 0.01):
        q1 = 2 - 0.0162*Ed*Ed - 0.1667*Ed + 0.185*Ed*Eb - 0.6667*Eb - 0.037*Eb*Eb
        q2 =   - 0.111*Eb*Eb - 0.1398*Eb*Ed - 0.25*Ed - 0.33*Eb + 2
        lambd.append([Ed,Eb])
        QoS.append([q1,q2])
        
lambdA2 = np.array(lambd)
QoSA2 = np.array(QoS)



fig = plt.figure(figsize = (15,15))
ax = fig.add_subplot(111, projection='3d')
ax.view_init(90,0)
ax.set_xlabel("Expected lambda1")
ax.set_ylabel("Expected lambda2")
ax.set_zlabel("Expected QoS1")
scatter0 = ax.scatter(lambdA0[:,0], lambdA0[:,1], QoSA0[:,1], s = 0.5, c =  'cyan')
scatter1 = ax.scatter(lambdA1[:,0], lambdA1[:,1], QoSA1[:,1], s = 0.5, c =  'orange')
scatter2 = ax.scatter(lambdA2[:,0], lambdA2[:,1], QoSA2[:,1], s = 0.5, c =  'green')
ax.legend([scatter0, scatter1, scatter2], ['Both lamda1 and lambda2 are individual expectations', 'lambda1 and lambda2 are total and individual expectations', 'both lambda1 and lambda2 are total expectations'])

        
        
    
    

