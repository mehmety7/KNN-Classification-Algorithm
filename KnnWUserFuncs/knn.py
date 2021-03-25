# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 00:15:27 2020

@author: mehmet
"""

"""
x_train -- bağımısız değişkenlerin olduğu öğrenme seti
y_train -- bağımlı değişkenlerin olduğu öğrenme seti
x_test -- bağımısız değişkenlerin olduğu test seti
y_test -- bağımlı değişkenlerin olduğu test seti
y_pred -- bağımlı değişkenlerin olduğu tahmin seti
"""

import math

def is_str(v):
    return type(v) is str

def bubbleSort(list1):
    n = len(list1) 
    for i in range(n-1): 
        for j in range(0, n-i-1): 
            if list1[j] > list1[j+1] : 
                list1[j], list1[j+1] = list1[j+1], list1[j]
    return list1

def hamming(x,y):
    if x == y:
        return 1
    else:
        return 0    

def distance(x,y):
    sum = 0
    for i in range(0, len(x)):
        if(is_str(x[i])):
            sum = sum + hamming(x[i], y[i])
        else:
            sum = sum + (x[i] - y[i])**2
    result = math.sqrt(abs(sum))
    return result

def accuracy_rate(test, preds):
    all_data = len(test)
    match_number = 0
    for i in range(0, all_data):
        if test[i] == preds[i]:
            match_number+=1
    return match_number/all_data 

class KNN():
    
    def fit(self, x_train, y_train):
        self.x_train = x_train
        self.y_train = y_train
    
    def predict(self, x_test, k):        
        predictions = []
        for record in x_test:
            label = self.closest(record, k)
            predictions.append(label)
        return predictions
    
    def closest(self, record, k):
        global i,j
        if k == 1:
            best_dist = distance(record, self.x_train[0])
            best_index = 0
            for i in range(1, len(self.x_train)):
                dist = distance(record, self.x_train[i])
                if dist < best_dist:
                    best_dist = dist
                    best_index = i
            return self.y_train[best_index]
        else:
            distances = []
            neighbors = []
            for j in range(0, len(self.x_train)):
                distances.append(distance(record, self.x_train[j]))
            
            bubbleSort(distances)
            del distances[k:]
            for i in range(0, len(distances)):    
                for j in range(0, len(self.x_train)):
                    if distances[i] == distance(record, self.x_train[j]):
                        neighbors.append(self.y_train[j]);
            return self.kNearest(neighbors)
    
    def kNearest(self, list1):
        n = len(list1)
        mostCountLabel = list1[0]
        mostCount = list1.count(list1[0]) 
        for i in range(1, n):
            if list1.count(list1[i]) > mostCount:
                mostCount = list1.count(list1[i])
                mostCountLabel = list1[i]
        return mostCountLabel
            

x_train = [['uzun',190,85,45],
           ['kısa',185,75,43],
           ['kısa',188,78,40],
           ['uzun',169,60,46],
           ['kısa',165,58,37],
           ['uzun',170,60,36],
           ['uzun',155,45,35],
           ['uzun',159,63,36]]
y_train = ['e','e','e','e','k','k','k','k']
x_test = [['kısa',195,100,46],
           ['uzun',140,36,33],
           ['uzun',174,78,40],
           ['kısa',206,105,47],
           ['kısa',168,68,37],
           ['uzun',174,58,38],
           ['uzun',152,43,34],
           ['uzun',161,63,36]]
y_test = ['e','k','e','e','k','k','k','e']
y_preds = []


k = int(input("k degeri giriniz: "))
sample = KNN()
sample.fit(x_train,y_train)
y_preds = sample.predict(x_test, k)
print(y_preds)
print(accuracy_rate(y_test,y_preds))

"""
x_train -- bağımısız değişkenlerin olduğu öğrenme seti
y_train -- bağımlı değişkenlerin olduğu öğrenme seti
x_test -- bağımısız değişkenlerin olduğu test seti
y_test -- bağımlı değişkenlerin olduğu test seti
y_pred -- bağımlı değişkenlerin olduğu tahmin seti
"""
    
            
    
        
        
    