#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:42:22 2018

@author: gdn417
"""
import numpy as np
import matplotlib.pyplot as plt


def Kmeans(data, K):

    
    # pick K random centroids 
    # TO BE CONTINUED... SEE IF THERE IS A BETTER WAY TO PICK RANDOM CENTRIOD COORDINATES
    #K_coord = np.hstack((np.asarray(np.random.normal(0, 10, K)).reshape(K,1), np.asarray(np.random.normal(0, 10, K)).reshape(K,1)))
    K_coord = np.random.rand(K,2)*10
    print(K_coord)
    #print(K_coord)
    
    epsilon = 0.1
    diff = 100
    while(epsilon < diff):
    
        # label each data point to the closest centroid.
        label = []
        for i in range(0,data.shape[0]):
            dist = []
            for j in range(0,K_coord.shape[0]):
                # calculate euclidian distance from each data point to centriod
                dist.append(np.sqrt( (data[i,0] - K_coord[j,0])**2 + (data[i,1] - K_coord[j,1])**2 ))
            #print(dist)
            label.append(np.argmin(dist))
        
        #print(label)
    
        # calculate new coordinates for each centroid by finding the
        # coordinate average for every data point labelled to the specific centroid 
        # 
        new_K_coord = np.zeros([K,2]) # allocate data for new K centriod coordinates
        for i in range(0,K):
            sumCoords = np.zeros([data.shape[0],2])
            countMembers = label.count(i)
            #print(countMembers)
            for j in range(0,data.shape[0]):

            
                # add coordinates for each data point belonging to a specific label
                if label[j] == i:
                    sumCoords[j,:] = data[j,:]
            
        
            # set new coordinates
            new_K_coord[i,] = np.sum(sumCoords, axis = 0)/countMembers
        
        
    
    
        # calculate differences between new and old centriod coordinates to be used for epsilon
        diff = np.mean(abs(new_K_coord - K_coord))
        K_coord = new_K_coord

    
    
    return K_coord, np.hstack((data,np.asarray(label).reshape(data.shape[0],1)))



### main ####
#np.random.seed(8)

# generate test data
clust1 = np.hstack((np.asarray(np.random.normal(1, 1, 20)).reshape(20,1), np.asarray(np.random.normal(10, 1, 20)).reshape(20,1)))
clust2 = np.hstack((np.asarray(np.random.normal(10, 1, 20)).reshape(20,1), np.asarray(np.random.normal(1, 1, 20)).reshape(20,1)))
clust3 = np.hstack((np.asarray(np.random.normal(5, 1, 20)).reshape(20,1), np.asarray(np.random.normal(5, 1, 20)).reshape(20,1)))
clust4 = np.hstack((np.asarray(np.random.normal(30, 1, 20)).reshape(20,1), np.asarray(np.random.normal(30, 1, 20)).reshape(20,1)))
clust5 = np.hstack((np.asarray(np.random.normal(80, 1, 20)).reshape(20,1), np.asarray(np.random.normal(8, 1, 20)).reshape(20,1)))
clust6 = np.hstack((np.asarray(np.random.normal(3, 1, 20)).reshape(20,1), np.asarray(np.random.normal(13, 1, 20)).reshape(20,1)))

data = np.vstack((clust1,clust2,clust3,clust4,clust5,clust6))

#print(data)



#print(Kmeans(data, 5))
kmeans, labelledData = Kmeans(data, 3)
print(labelledData)
print(kmeans)
# plot test data

plt.plot(data[:,0], data[:,1], 'ro', kmeans[:,0], kmeans[:,1], 'bo')
