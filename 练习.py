# def panduanrunnian(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return True
#     return False
# year = int(input())
# if panduanrunnian(year):
#     print(f'{year}年是闰年' )
# else:
#     print(f'{year}年不是闰年')
#
#
# a = input().split('，')
# for i in a:
#     print(f'{i.strip()}，你好！')
#
#
# count = 0
# min1,max1  = map(int,input().split())
# for i in range(min1,max1+1):
#     if i % 3 == 0 and i % 5 == 0 and i % 7 == 0:
#        count = count + 1
# print(count)

# B2010
# # a,b = map(int,input().split())
# # c = a//b
# # d = a%b
# # print(c,d)


# B2011
# a,b = map(int,input().split())
# c = a/b
# print("%.9f"%c)

# B2012
# a = float(input())
# b = float(input())
# c = b/a*100
# print("%.3f%%"%c)

# B2013
# a = float(input())
# c = 5*(a-32)/9
# print("%.5f"%c)

# B2014
# r = float(input())
# d = r*2
# c = 3.14159*d
# s = 3.14159*r*r
# print("%.4f"%d,"%.4f"%c,"%.4f"%s)

# B2015
# a,b = map(float,input().split())
# c = 1/a
# d = 1/b
# e = c+d
# r = 1/e
# print("%.2f"%r)

# B2016
# a = float(input())
# a = int(a)
# print(a)

# B2017
# a = ord(input().strip())
# print(a)

# B2018
# a = int(input().strip())
# a = chr(a)
# print(a)

# B2019
# a = input()
# a=int(bool(int(a)));
# print(a)

# B2020
# a,b,c,d,f = map(int,input().split())
# numa1 = a//3
# numa2 = a%3
# numb1 = (b+numa1)//3
# numb2 = (b+numa1)%3
# numa1 += numb1
# numc1 = (c+numb1)//3
# numc2 = (c+numb1)%3
# numb1 += numc1
# numd1 = (d+numc1)//3
# numd2 = (d+numc1)%3
# numc1 += numd1
# numf1 = (f+numd1+numa1)//3
# numf2 = (f+numd1+numa1)%3
# numd1 += numf1
# numa1 += numf1
# print(numa1,numb1,numc1,numd1,numf1)
# print(numa2+numb2+numc2+numd2+numf2)

# B2021
# a = float(input())
# print(f'%.3f'%a)

# B2023
# a = input().strip()
# b = int(input())
# c = float(input())
# d = float(input())
# print(a,b,"%.6f"%c,"%.6f"%d)

# B2024
# a = float(input())
# print(f'%f'%a)
# print(f'%.5f'%a)
# print(f'%e'%a)
# print(f"%g"%a)

# B2025
# print("  *")
# print(" ***")

# print("*****")
# print(" ***")
# print("  *")

# B2026
# a,b = input().split()
# a = float(a)
# b = float(b)
# c = a % b
# print("%.4f"%c)

# B2027
# r = int(input())
# v = (4/3)*3.14*r**3
# print("%.5f"%v)

# B2028
# a = input()
# print(a[::-1])

# B2029
# from math import ceil
# h,r = map(int,input().split())
# v = 3.14*r*r*h
# num = 20000/v
# print(ceil(num))
#
# B2030
from math import  sqrt
# x1,y1 = map(float,input().split())
# x2,y2 = map(float,input().split())
# chang = ((x1-x2)**2+(y1-y2)**2)**(1/2)
# print("%.3f"%chang)

# import numpy as np

# print(np.array([1, 2, 3, 4]))