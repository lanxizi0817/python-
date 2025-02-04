#12.18
'''题单【入门1】分支结构'''
# import math
# #P2433
# n = int(input())
#
# if n == 1:
#     #问题1
#     print("I love Luogu!")
# elif n == 2:
#     #问题2
#     A = 2 + 4
#     B = 10 - A
#     print(f'{A} {B}')
# elif n == 3:
#     #问题3
#     C = 14 // 4
#     D = C * 4
#     E = 14 - D
#     print(C)
#     print(D)
#     print(E)
# elif n == 4:
#     #问题4
#     F = 500 / 3
#     print(f'{F:.3f}')
# elif n == 5:
#     #问题5
#     v = 12 + 20
#     s = 260 + 220
#     t = s / v
#     print(int(t))
# elif n == 6:
#     #问题6
#     G = math.sqrt(6*6+9*9)
#     print(f'{G:.4f}')
# elif n == 7:
#     #问题7
#     print("110\n90\n0")
# elif n == 8:
#     #问题8
#     a = 3.141593*10
#     print(f'{a:.4f}')
#     b = 3.141593*25
#     print(f'{b:.4f}')
#     c = 3.141593*(500/3.0)
#     print(f'{c:.3f}')
# elif n == 9:
#     print(22)
# elif n == 10:
#     print(9)
# elif n == 11:
#     i = 100/3
#     print(f'{i:.4f}')
# elif n == 12:
#     print("13\nR")
# elif n == 13:
#     H = (3.141593*4*4*4)*(4/3)
#     I = (3.141593*10*10*10)*(4/3)
#     K = (H + I)**(1/3)
#     print(int(K))
# elif n == 14:
#     a = 1
#     b = -120
#     c = 3500
#
#     # 计算判别式
#     discriminant = b ** 2 - 4 * a * c
#
#     # 计算两个解
#     x1 = (-b + math.sqrt(discriminant)) / (2 * a)
#     x2 = (-b - math.sqrt(discriminant)) / (2 * a)
#
#     # 取两个解中较小的一个，并四舍五入到最近的整数
#     price = round(min(x1, x2))
#
#     # 输出结果
#     print(price)

#P5709
# m,t,s = map(int,input().split())
# if t == 0:
#     num = 0
# else:
#     if s//t == 0:
#         num = m - (s / t - 1)
#     else:
#         num = m - (s / t)
# num = max(num,0)
# print(int(num))

#P5710
# x = int(input())
# A,B,C,D = 0,0,0,0
# if 0 <= x <= 1000:
#     if x % 2 == 0 and (4 < x <= 12):
#         A = 1
#     if (x % 2 == 0 and (4 < x <= 12)) or x % 2 == 0 or (4 < x <= 12):
#         B = 1
#     if (x % 2 == 0 and not (4 < x <= 12)) or (not x % 2 == 0 and 4 < x <= 12):
#         C = 1
#     if x % 2 != 0 and (x<=4 or x>12):
#         D = 1
# print(f'{A} {B} {C} {D}')

#P5711
# def panduanrunnian(year):
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         return 1
#     return 0
# year = int(input())
# print(panduanrunnian(year))

#P5712
# x = int(input())
# if 0 <= x <= 100:
#     if x == 1 or x == 0 :
#         print(f"Today, I ate {x} apple.")
#     if x > 1:
#         print(f"Today, I ate {x} apples.")

#P5713
# n = int(input())
# if 1 <= n <= 100:
#     t1 = 5 * n
#     t2 = 11 + 3 * n
#     if t1 < t2:
#         print("Local")
#     else:
#         print("Luogu")

#P5714
# m , h= map(float,input().split())
# if 40 <= m <= 120 and 1.4 <= h <= 2.0:
#     num = m/(h*h)
#     if num < 18.5:
#         print("Underweight")
#     if 18.5 <= num < 24:
#         print("Normal")
#     if num >= 24:
#         print(f"{num:.6g}")
#         print("Overweight")
#P5715
# a , b , c= map(int,input().split())
# d = sorted([a,b,c])
# print(' '.join(map(str,d)))

#P5716
# y , m = map(int,input().split())
# d = 0
# if 1583 <= y <= 2020 and 1 <= m <= 12:
#     if (y % 4 == 0 and y % 100 != 0) or (y % 400 == 0):
#         if m in [2]:
#             d = 29
#         elif m in [1,3,5,7,8,10,12]:
#             d = 31
#         else:
#             d = 30
#     else:
#         if m in [2]:
#             d = 28
#         elif m in [1,3,5,7,8,10,12]:
#             d = 31
#         else:
#             d = 30
#     print(d)

#P1085
# m = -1
# d = 0
# for i in range(1,8):
#     s , o = map(int,input().split())
#     t = s + o
#     if t > 8 :
#        if m == -1 or t > m or (t == m and i < d):
#            m = t
#            d = i
# if m == -1:
#     print(0)
# else:
#     print(d)

#P1909
