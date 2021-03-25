# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd


veriler=pd.read_csv("veriler.csv")

from sklearn.preprocessing import LabelEncoder
#label encoder ile numerik olmayan ülke kolonunu numerik verilere dönüştürdük
le=LabelEncoder()
veriler['ulke']=le.fit_transform(veriler['ulke'])

#bağımlı ve bağımsız verileri belirttik
bagimli=veriler['cinsiyet']
bagimsiz=veriler.iloc[:,0:4]

#verileri eğitim ve test olarak ayırdık, eğitim kısmı test kısmının iki katı olacak.
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(bagimsiz,bagimli,test_size=0.33,random_state=0)

# KNeighborsClassifier sınıfını import ettik
from sklearn.neighbors import KNeighborsClassifier

# KNeighborsClassifier sınıfından bir nesne ürettik
# n_neighbors : K değeridir. En yakınındaki kaç elemana bakacağımızı bu sayı belirler. Default değeri 3'tir.
# metric : Değerler arasında uzaklık hesaplama formülüdür.öklitde verebiliriz

knn = KNeighborsClassifier(n_neighbors=3,metric='minkowski')

# Makineyi eğitiyoruz
knn.fit(x_train,y_train)

# Test veri kümemizi verdik ve tahmin etmesini sağladık
result = knn.predict(x_test)

# Karmaşıklık matrisi
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test,result)
print(cm)

# Başarı Oranı
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(y_test, result)


from sklearn import metrics
y_pred=result
print(metrics.classification_report(y_test,y_pred))
