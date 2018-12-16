#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 30 00:08:54 2018

@author: Nelson
"""
import numpy as np
import matplotlib.pyplot as plt

def calc_delta(x):
    
    N = len(x)
    return N*np.sum(np.square(x)) - np.square(np.sum(x))

def calc_A(x, y):
    
    den = calc_delta(x)
    num = np.sum(np.square(x))*np.sum(y) - np.sum(x)*np.sum(x*y)
                
    return num / den


def calc_B(x, y):
    
    N = len(x)
    
    den = calc_delta(x)
    num = N*np.sum(x*y) - np.sum(x)*np.sum(y)
    
    return num / den

def calc_sigmaY(x, y):
    
    A = calc_A(x,y)
    B = calc_B(x,y)
    N = len(x)
    
    sig_sq = 1.0/(N-2)*np.sum(np.square(y-(A+B*x)))
    
    return np.sqrt(sig_sq)

def calc_sigmaA(x, y):
    
    sigmaY = calc_sigmaY(x,y)
    delta = calc_delta(x)
    
    sigmaA = sigmaY*np.sqrt(np.sum(np.square(x))/delta)
    
    return sigmaA

def calc_sigmaB(x, y):
    
    sigmaY = calc_sigmaY(x,y)
    N = len(x)
    delta = calc_delta(x)
    
    sigmaB = sigmaY*np.sqrt(N/delta)
    
    return sigmaB

def report(x, y):
    
    print("-------summary EX3------")
    print("A = %.3f" % calc_A(x,y))
    print("B = %.3f" % calc_B(x,y))
    print("sigY_sq = %.3f" % np.square(calc_sigmaY(x,y)))
    print("sigmaA = %.3f" % calc_sigmaA(x,y))
    print("sigmaB = %.3f" % calc_sigmaB(x,y))
    print("-----------end----------")


def simpleLineFit(x, y):
    
    # plot all the dots first
    plt.plot(x, y, '.')
    
    # plot the least-squares-line
    
    A = calc_A(x,y)
    B = calc_B(x,y)
    y_fit = A + B*x
    
    plt.plot(x, y_fit, '-')
    

x = np.array([79, 82, 85, 88, 90])
y = np.array([8, 17, 30, 37, 52])

simpleLineFit(x,y)
report(x,y)
