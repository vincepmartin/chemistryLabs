# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:26:51 2015

@author: vmartin
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib.patches import Ellipse

#Plot A
figureA = plt.figure()

A_Volume_Trial1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22]
A_Conductivity_Trial1 = [10185,9155,8359,7490,6595,5755,4862,4033,3232,2390,1516,715,34,1285,2293,3245,4114,4988,5788,6435,7153,7805,8497]


A_Volume_Trial2 = [10, 10.2,10.4,10.6,10.8,11,11.2,11.4,11.6,11.8,12,12.2,12.4,12.6,12.8,13]
A_Conductivity_Trial2 = [1597,1428,1203,1029,827,697,482,183,87,63,367,502,833,1050,1311,1522]

B_Volume_Trial1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
B_Conductivity_Trial1 = [2585,2505,2440,2382,2313,2254,2170,2166,2112,2085,2058,2007,2049,2239,2387,2538,2680]

B_Volume_Trial2 = [9,9.2,9.4,9.6,9.8,10,10.2]
B_Conductivity_Trial2 = [2021,2010,1998,1991,2013,2034,2059]

def has_equal_element(list1, list2):
    return any(e1 == e2 for e1, e2 in zip(list1, list2))

def calculate_molarity(mLSolution):
    

def line_slope(x,y):
    rise = y[-1]- y[0]
    run = x[-1] - x[0]
    
    print("Rise is ", rise)
    print("Rrun is ", run)
    
    
    slope = rise/run
    return slope
    
def overlappingCoords(m1, b1, m2, b2):
    overlappingX = (b2-b1)/(m1-m2)
    
    return overlappingX
    
    

def plotDualLinearRegression(X, Y, Experiment, TrialNumber):
    #find the min value of Y
    indexOfSmallestY = np.argmin(Y)
    plotTitle = "Experiment " + Experiment + " Trial " + TrialNumber
    
    el = Ellipse((2, -1), 0.5, 0.5)


    A_coefficients = np.polyfit(X[0:indexOfSmallestY+1], Y[0:indexOfSmallestY+1], 1)
    B_coefficients = np.polyfit(X[indexOfSmallestY-1:], Y[indexOfSmallestY-1:], 1)
    A_polynomial = np.poly1d(A_coefficients)
    B_polynomial = np.poly1d(B_coefficients)
    A_ys = A_polynomial(X[0:indexOfSmallestY+1])
    B_ys = B_polynomial(X[indexOfSmallestY-1:])
    
    plt.plot(X[0:indexOfSmallestY+1],A_ys)
    plt.plot(X[indexOfSmallestY-1:],B_ys)
    
    plt.title(plotTitle, weight='bold')
    plt.xlabel("mL of Solution")
    plt.ylabel(r'$\mu$S/cm Conductivity')
    
    plt.scatter(X,Y)
    
    #print("line_slope_X:", X[0:indexOfSmallestY+1])
    #print("line_slope_Y:" , A_ys)
    
    slopeLine1 = line_slope(X[0:indexOfSmallestY+1], A_ys)
    slopeLine2 = line_slope(X[indexOfSmallestY-1:], B_ys)
    yintLine1 = A_ys[0] - (slopeLine1 * X[0])
    yintLine2 = B_ys[0] - (slopeLine2 * X[indexOfSmallestY-1])
    
    overlappingX = overlappingCoords(slopeLine1, yintLine1, slopeLine2, yintLine2)
    #print("slopeLine1 is",slopeLine1)
    #print("slopeLine2 is", slopeLine2)
    #print("yintLine1 is", yintLine1)
    #print("yintLine2 is", yintLine2)    
    #print("Over lapping X is", overlappingX)
    
    overlappingY = slopeLine1*overlappingX + yintLine1
    
    roundedOverLappingX = format(overlappingX,'.2f')
    mLSolOfEq = "Equiv: " + roundedOverLappingX + "mL"
    
    #x_overlap = overlappingCoords(slopeLine1, yintLine1, slopeLine2, yintLine2)
    
    plt.annotate(mLSolOfEq, xy=(overlappingX, overlappingY),  xycoords='data',
                xytext=(-120, -20), textcoords='offset points',
                size=10,
                arrowprops=dict(arrowstyle="wedge,tail_width=0.3",
                                fc="0.6", ec="none",
                                patchB=el,
                               connectionstyle="arc3,rad=-0.4"),
                )
    
    plt.savefig("Exp"+Experiment+"Trial"+TrialNumber+".png", dpi = 300)


plt.figure(1)
plotDualLinearRegression(A_Volume_Trial1,A_Conductivity_Trial1, "A", "1")
plt.figure(2)
plotDualLinearRegression(A_Volume_Trial2,A_Conductivity_Trial2, "A", "2")
plt.figure(3)
plotDualLinearRegression(B_Volume_Trial1,B_Conductivity_Trial1, "B", "1")
plt.figure(4)
plotDualLinearRegression(B_Volume_Trial2,B_Conductivity_Trial2, "B", "2")

