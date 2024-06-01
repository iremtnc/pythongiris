# -*- coding: utf-8 -*-
"""
Created on Sat Jun  1 15:28:39 2024

@author: itsme
"""

import math

# Noktaların Tanımlanması
points = [(1, 2), (4, 6), (5, 1), (7, 8), (2, 3)]

# Öklid Mesafesi İçin Bir Fonksiyon Yazma
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Mesafelerin Hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append(distance)

# Minimum Mesafenin Bulunması
min_distance = min(distances)

# Sonucu Yazdırma
print("Minimum Mesafe:", min_distance) 

