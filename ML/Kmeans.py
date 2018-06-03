#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  1 14:42:22 2018

@author: André Vidas Olsen
"""
import numpy as np
import matplotlib.pyplot as plt


def Kmeans1(data, K):

    
    # pick K random centroids 
    # TO BE CONTINUED... SEE IF THERE IS A BETTER WAY TO PICK RANDOM CENTRIOD COORDINATES
    #K_coord = np.hstack((np.asarray(np.random.normal(0, 10, K)).reshape(K,1), np.asarray(np.random.normal(0, 10, K)).reshape(K,1)))
    K_coord = np.random.rand(K,data.shape[1])*10

    
    epsilon = 0.1 # iteration threshold
    diff = 100 # initialize difference between centriod position between iterations
    while(epsilon < diff):
    
        #### label each data point to the closest centroid
        label = []
        for i in range(0,data.shape[0]):
            dist = []
            
            for j in range(0,K_coord.shape[0]):
                # calculate euclidian distance from each data point to centriod
                innerPart = 0
                for k in range(0,data.shape[1]):
                    #dist.append(np.sqrt( (data[i,2*k] - K_coord[j,2*k])**2 + (data[i,2*k+1] - K_coord[j,2*k+1])**2 ))
                    innerPart += (data[i,k] - K_coord[j,k])**2
                
                dist.append(np.sqrt(innerPart))
            
            # determine which centriod the given data point should be labelled with 
            label.append(np.argmin(dist))
        
    
        # calculate new coordinates for each centroid by finding the
        # coordinate average for every data point labelled to the specific centroid 
        new_K_coord = np.zeros([K,data.shape[1]]) # allocate data for new K centriod coordinates
        for i in range(0,K):
            sumCoords = np.zeros([data.shape[0],data.shape[1]])
            countMembers = label.count(i)

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


def Kmeans2(data, K):
    K_coord = np.random.rand(K,2)*10
    
    epsilon = 0.1 # iteration treshold
    diff = 100 
    while(epsilon < diff):
        label = []
        sumCoords = np.zeros([data.shape[0], 2*K])
        #### find label for each data point and find new centriod 
        for i in range(data.shape[0]):
            dist = []
            for j in range(K):
                # calculate euclidian distance from each data point to centriod
                dist.append(np.sqrt( (data[i,0] - K_coord[j,0])**2 + (data[i,1] - K_coord[j,1])**2 ))
        
            # determine which centriod the given data point should be labelled with 
            label.append(np.argmin(dist))
            sumCoords[i,2*np.argmin(dist)] = data[i,0]
            sumCoords[i,2*np.argmin(dist)+1] = data[i,1]
    

        new_K_coord = np.zeros([K,2]) # allocate data for new K centriod coordinates
        for i in range(K):
            countMembers = label.count(i)
            # set new coordinates
            new_K_coord[i,] = np.sum(sumCoords[:,2*i:(2*i+2)], axis = 0)/countMembers
            
        
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

#data = np.vstack((clust1,clust2,clust3,clust4,clust5,clust6))
data = np.vstack((clust1,clust2))




#kmeans, labelledData = Kmeans1(data, 2)
#kmeans, labelledData = Kmeans2(data,6)
#print(labelledData)
#print(kmeans)

# plot test data
#plt.plot(data[:,0], data[:,1], 'ro')
#plt.plot(data[:,0], data[:,1], 'ro', kmeans[:,0], kmeans[:,1], 'bo')




import time

# generate test datas
clust1 = np.hstack((np.asarray(np.random.normal(1, 1, 20000)).reshape(20000,1), np.asarray(np.random.normal(10, 1, 20000)).reshape(20000,1)))
clust2 = np.hstack((np.asarray(np.random.normal(10, 1, 20000)).reshape(20000,1), np.asarray(np.random.normal(1, 1, 20000)).reshape(20000,1)))
data = np.vstack((clust1,clust2))

#start = time.time()
#Kmeans2(data, 2)
#stop = time.time()
#print(stop-start)


#start = time.time()
#Kmeans1(data, 2)
#stop = time.time()
#print(stop-start)






# test for n-space implementation

clust1 = np.hstack((np.asarray(np.random.normal(1, 1, 20)).reshape(20,1), np.asarray(np.random.normal(10, 1, 20)).reshape(20,1), np.asarray(np.random.normal(-10, 1, 20)).reshape(20,1), np.asarray(np.random.normal(-10, 1, 20)).reshape(20,1)))
clust2 = np.hstack((np.asarray(np.random.normal(1, 1, 20)).reshape(20,1), np.asarray(np.random.normal(-10, 1, 20)).reshape(20,1), np.asarray(np.random.normal(10, 1, 20)).reshape(20,1), np.asarray(np.random.normal(10, 1, 20)).reshape(20,1)))

data = np.vstack((clust1,clust2))

kmeans, labelledData = Kmeans1(data, 2)

print(kmeans)
print(labelledData)
