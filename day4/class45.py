# -*- coding: utf-8 -*-
"""
Created on Thu Jan 28 14:21:12 2021

@author: USER
"""
A =[10,25,31,3,4,5,7,2,1]
for i in range (len(A)):
    for j in range(len(A)):
        if A[i]<A[j]:
            T = A[i]
            A[i] = A[j]
            A[j] = T
print(A)