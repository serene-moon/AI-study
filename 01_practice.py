'''20201028 인공지능 실습 과제'''
'''세 점이 주어질 때 한 점과 직선 사이의 거리와 두 직선 사이의 각 구하기'''

import time
import random
import math
import numpy as np
import matplotlib.pyplot as plt

def dist_AtoBC(arr):
    x1, y1 = arr[0]
    x2, y2 = arr[1]
    x3, y3 = arr[2]
    a = y3 - y2
    b = x2 - x3
    c = x3 * y2 - x2 * y3
    d = abs(a * x1 + b * y1 + c) / math.sqrt(a ** 2 + b ** 2)
    return d

def angl_B(arr):
    BA = arr[0] - arr[1]
    BC = arr[2] - arr[1]
    _BA_ = math.sqrt(BA[0] ** 2 + BA[1] ** 2)  # vector magnitude
    _BC_ = math.sqrt(BC[0] ** 2 + BC[1] ** 2)
    ip = BA[0] * BC[0] + BA[1] * BC[1]  # inner product
    cosA = ip / (_BA_ * _BC_)
    B = math.acos(cosA)  # radian
    degB = math.degrees(B)
    return degB

start = time.time()


lst = [random.randrange(-100,100) for i in range(6)]
x1, y1, x2, y2, x3, y3 = lst

print('A ( {} , {} ) \nB ( {} , {} ) \nC ( {} , {} )'.format(x1,x2,y1,y2,x3,y3))

# 점 A에서 선 BC까지의 거리 구하기
a = y3 - y2
b = x2 - x3
c = x3*y2 - x2*y3
d = abs(a*x1 + b*y1 + c) / math.sqrt(a**2 + b**2)
print('점 A에서 선 BC까지의 거리 :', d)

#각도 B 구하기
BA = ( x1 - x2 , y1 - y2 )
BC = ( x3 - x2 , y3 - y2 )
_BA_ = math.sqrt( BA[0]**2 + BA[1]**2 ) #vector magnitude
_BC_ = math.sqrt( BC[0]**2 + BC[1]**2 )
ip = BA[0]*BC[0] + BA[1]*BC[1] # inner product
cosA = ip / ( _BA_ * _BC_ )
B = math.acos(cosA) # radian
degB = math.degrees(B)
print('각 B의 크기 :',degB,'도')

print()

# 추가 과제
arrPoint = np.random.randint(-100,100, size=(3,2))

print('점 A, B, C의 좌표 : \n', arrPoint)
print('점 A에서 선 BC까지의 거리 :',dist_AtoBC(arrPoint))
print('각 B의 크기 :',angl_B(arrPoint),'도')


lst = input('\n숫자 6개 입력 : ').split()
lst = [int(lst[i]) for i in range(6)]
arrPoint = np.array(lst)
arrPoint = arrPoint.reshape(3,2)

print('점 A, B, C의 좌표 : \n', arrPoint)
print('점 A에서 선 BC까지의 거리 :',dist_AtoBC(arrPoint))
print('각 B의 크기 :',angl_B(arrPoint),'도')

x = [arrPoint[i][0] for i in range(3)]
y = [arrPoint[i][1] for i in range(3)]
plt.scatter(x, y)

print('\nProcessing time :', time.time() - start)

plt.show()