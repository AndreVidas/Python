#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:42:22 2018

@author: gdn417
"""
import numpy as np



def Kmeans(data, K):
    
    
    
    # pick K random centroids 
    K_coord = np.random.rand(K,2)*10
    
    
    # label each data point to the closest centroid.
    label = []
    for i in range(data.shape[0]):
        dist = []
        for j in range(K_coord.shape[0]):
            # calculate euclidian distance from each data point to centriod
            dist.append(np.sqrt( (data[i,0] - K_coord[j,0])**2 + (data[i,1] - K_coord[j,1])**2 ))
        label.append(np.argmin(dist))
        
        
    
    # calculate new coordinates for each centroid by finding the average
    # coordinate for every data points labelled to the specific centroid 
    # 
    new_K_coord = np.zeros([K,2]) # allocate data for new K centriod coordinates
    sumCoords = np.zeros([data.shape[0],2])
    for i in range(0,K):
        for j in range(0,data.shape[0]):
            #countMembers = label.count(j)
            if label[j] == i:
                sumCoords[j,:] = data[j,:]
            
    
        new_K_coord[i,] = np.sum(sumCoords, axis = 0)
    
    
          
    
    return np.hstack((data,np.asarray(label).reshape(data.shape[0],1)))



### main ####
np.random.seed(10)
data = np.random.rand(20,2)*10
#print(data)


#print(Kmeans(data, 5))
Kmeans(data, 3)