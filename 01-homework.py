import time

start = time.time()

import random
import math

lst = [random.randrange(-100,100) for i in range(6)]
x1, y1, x2, y2, x3, y3 = lst

print('A ( {} , {} ) \nB ( {} , {} ) \nC ( {} , {} )'.format(x1,x2,y1,y2,x3,y3))

# 점 A에서 선 BC까지의 거리 구하기
a = y3 - y2
b = x2 - x3
c = x3*y2 - x2*y3
d = abs(a*x1+b*y1+c) / math.sqrt(a**2+b**2)
print('점 A에서 선 BC까지의 거리 :',d)

#각도 B 구하기
ba = ( x1 - x2 , y1 - y2 )
bc = ( x3 - x2 , y3 - y2 )
labl = math.sqrt( ba[0]**2 + ba[1]**2 ) #vector magnitude
lacl = math.sqrt( bc[0]**2 + bc[1]**2 )
ip = ba[0]*bc[0] + ba[1]*bc[1] # inner product
cosa = ip / ( labl * lacl )
b = math.acos(cosa) # radian
degb = math.degrees(b)
print('각 B의 크기 :',degb,'도')

# 추가 과제
import numpy as np

arr = np.random.randint(-100,100, size=(3,2))

def dist_atobc(arr):
    x1, y1 = arr[0]
    x2, y2 = arr[1]
    x3, y3 = arr[2]
    a = y3 - y2
    b = x2 - x3
    c = x3 * y2 - x2 * y3
    d = abs(a * x1 + b * y1 + c) / math.sqrt(a ** 2 + b ** 2)
    return d

def angl_b(arr):
    ba = arr[0] - arr[1]
    bc = arr[2] - arr[1]
    labl = math.sqrt(ba[0] ** 2 + ba[1] ** 2)  # vector magnitude
    lacl = math.sqrt(bc[0] ** 2 + bc[1] ** 2)
    ip = ba[0] * bc[0] + ba[1] * bc[1]  # inner product
    cosa = ip / (labl * lacl)
    b = math.acos(cosa)  # radian
    degb = math.degrees(b)
    return degb

print(arr)
print('점 A에서 선 BC까지의 거리 :',dist_atobc(arr))
print('각 B의 크기 :',angl_b(arr),'도')

lst = input('숫지 6개 입력 : ').split()
lst = [int(lst[i]) for i in range(6)]
arr = np.array(lst)
arr = arr.reshape(3,2)
print(arr)

import matplotlib.pyplot as plt

x = [arr[i][0] for i in range(3)]
y = [arr[i][1] for i in range(3)]
plt.scatter(x,y)
plt.show()

print('time :', time.time() - start)