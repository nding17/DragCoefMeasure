#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 11:22:07 2018

@author: Nelson
"""

import numpy as np
import matplotlib.pyplot as plt

def calc_delta(w, x):
    
    return np.sum(w)*np.sum(w*np.square(x)) - np.square(np.sum(w*x))

def calc_A(x, y, w):
    
    num = np.sum(w*np.square(x))*np.sum(w*y) - np.sum(w*x)*np.sum(w*x*y)
    den = calc_delta(w,x)
            
    return num / den

def calc_B(x, y, w):
    
    num = np.sum(w)*np.sum(w*x*y) - np.sum(w*x)*np.sum(w*y)
    den = calc_delta(w,x)
    
    return num / den

def calc_sigmaA(w, x):
    
    delta = calc_delta(w,x)
    return np.sqrt(np.sum(w*np.square(x)) / delta)

def calc_sigmaB(w, x):
    
    delta = calc_delta(w,x)
    return np.sqrt(np.sum(w) / delta)


def update_w(x, y, w, dx, dy):
    
    B = calc_B(x,y,w)
    print(B)
    for i in range(0, len(x)):
        # update weights 
        w[i] = 1.0 / (dy[i]**2 + (B*dx[i])**2)

def report(x, y, w):
    
    print("-------summary EX4------")
    print("A = %.3f" % calc_A(x,y,w))
    print("B = %.7f" % calc_B(x,y,w))
    print("sigmaA = %.3f" % calc_sigmaA(w,x))
    print("sigmaB = %.7f" % calc_sigmaB(w,x))
    print("-----------end----------")

x = np.array([298.68333333,  303.65, 308.28333333, 313.38333333, 
              318.28333333, 323.21666667, 328.25,  333.05, 
              338.11666667])
y = np.array([-0.02633333, -0.026, -0.027, -0.027, -0.028, -0.027, 
              -0.02933333, -0.02833333, -0.02866667])
dx = np.array([0.20275875, 0.25166115, 0.18559215, 0.18559215, 
               0.06666667, 0.06666667,0.05773503, 0.23094011, 
               0.08819171])
dy = np.array([0.00088192, 0.00057735, 0.00057735, 0.00057735, 
               0.00057735, 0.001, 0.00088192, 0.00033333, 
               0.00033333])
w = np.ones(len(x))

x1 = np.array([55.25, 60., 64.5, 69.85, 74.75, 85., 89.75])
y1 = np.array([-0.0275, -0.0315, -0.03, -0.0305, -0.03, -0.0295,-0.0305])
dx1 = np.array([0.25, 0.,   0.,   0.35, 0.25, 0.,   0.25])
dy1 = np.array([0.0005, 0.0005, 0.001,  0.0005, 0.,     0.0005, 0.0005])
w1 = np.ones(len(x1))

# do 4 iterations to get the best w's
for i in range(0, 3):
    #print(w)
    update_w(x,y,w,dx,dy)
    update_w(x1, y1, w1, dx1, dy1)
    
def simpleLineFit(x, y, w, dx, dy):
    
    plt.xlabel(r'Temperature (K)')
    plt.ylabel(r'$\Delta{V}$ (V)')   
    # plot all the dots first
    plt.plot(x, y, '.')
    
    # plot the least-squares-line
    
    A = calc_A(x,y,w)
    B = calc_B(x,y,w)
    y_fit = A + B*x
    
    plt.plot(x, y_fit, '-')
    plt.errorbar(x,y,dy,dx,fmt= 'ro')
    
# now our w's should be very nice 
#simpleLineFit(x1, y1, w1, dx1, dy1)
#report(x1,y1,w1)


simpleLineFit(x, y, w, dx, dy)
report(x,y,w)

