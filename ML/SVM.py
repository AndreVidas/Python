#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import numpy as np
import matplotlib.pyplot as plt
import cvxpy
    

#from cvxpy import *
#% matplotlib inline


# Define the two sets 
d = 2   # Dimension of problem. We'll leave at 2 for now.
m = 100 # Number of points in each class
n = 100  

x_center = [1,1]  # E.g. [1,1]
y_center = [3,1]  # E.g. [2,2]

# Set a seed which will generate feasibly separable sets
#  Note: these may only be separable with the default tutorial settings
np.random.seed(8)  

# Define random orientations for the two clusters
orientation_x = np.random.rand(2,2)
orientation_y = np.random.rand(2,2)

# Generate unit-normal elements, but clip outliers.
rx = np.clip(np.random.randn(m,d),-2,2)
ry = np.clip(np.random.randn(n,d),-2,2)
x = x_center + np.dot(rx,orientation_x)
y = y_center + np.dot(ry,orientation_y)
    
# Check out our clusters!
plt.scatter(x[:,0],x[:,1],color='blue')
plt.scatter(y[:,0],y[:,1],color='red')




## OPTIMIZATION- in CvxPy!

a = Variable(d)
b = Variable() 
t = Variable()

obj = Maximize(t)

x_constraints = [a.T * x[i] - b >= t  for i in range(m)]
y_constraints = [a.T * y[i] - b <= -t for i in range(n)]

constraints = x_constraints +  y_constraints + [norm(a,2) <= 1]

prob = Problem(obj, constraints)

prob.solve()
print("Problem Status: %s"%prob.status)




## Define a helper function for plotting the results, the decision plane, and the supporting planes

def plotClusters(x,y,a,b,t):
    # Takes in a set of datapoints x and y for two clusters,
    #  the hyperplane separating them in the form a'x -b = 0,
    #  and a slab half-width t
    d1_min = np.min([x[:,0],y[:,0]])
    d1_max = np.max([x[:,0],y[:,0]])
    # Line form: (-a[0] * x - b ) / a[1]
    d2_atD1min = (-a[0]*d1_min + b ) / a[1]
    d2_atD1max = (-a[0]*d1_max + b ) / a[1]

    sup_up_atD1min = (-a[0]*d1_min + b + t ) / a[1]
    sup_up_atD1max = (-a[0]*d1_max + b + t ) / a[1]
    sup_dn_atD1min = (-a[0]*d1_min + b - t ) / a[1]
    sup_dn_atD1max = (-a[0]*d1_max + b - t ) / a[1]

    # Plot the clusters!
    plt.scatter(x[:,0],x[:,1],color='blue')
    plt.scatter(y[:,0],y[:,1],color='red')
    plt.plot([d1_min,d1_max],[d2_atD1min[0,0],d2_atD1max[0,0]],color='black')
    plt.plot([d1_min,d1_max],[sup_up_atD1min[0,0],sup_up_atD1max[0,0]],'--',color='gray')
    plt.plot([d1_min,d1_max],[sup_dn_atD1min[0,0],sup_dn_atD1max[0,0]],'--',color='gray')
    plt.ylim([np.floor(np.min([x[:,1],y[:,1]])),np.ceil(np.max([x[:,1],y[:,1]]))])


# Typecast and plot these initial results

if type(a) == cvxpy.expressions.variables.variable.Variable: # These haven't yet been typecast
    a = a.value
    b = b.value
    t = t.value

plotClusters(x,y,a,b,t)