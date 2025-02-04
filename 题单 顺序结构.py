#12.16
'''题单【入门1】顺序结构'''
# a , b = map(int,input().split())
# print(int(a*b))

# a = input()
# print(a.upper())

# a = float(input())
# if 100 < a <1000:
#     a = str(a)
#     b = a[::-1]
#     print(b)

# ml,num = map(eval,input().split())
# mls = ml/num
# nums = num*2
# print("%.3f"%mls)
# print(nums)

# import math
# a , b , c = map(float,input().split())
# p = (a+b+c)/2
# s = math.sqrt(p*(p-a)*(p-b)*(p-c))
# print(f"{s:.1f}")

# def yyy(s, v):
#     t1 = s / v
#     available_time = 8 * 60 - 10 - t1
#     if available_time < 0:
#         available_time += 24 * 60
#     hours = int(available_time // 60)
#     minutes = int(available_time % 60)
#     return f"{hours:02d}:{minutes:02d}"
# s, v = map(int, input().split())
# print(yyy(s,v))

# a,b,c,d = map(int,input().split())
# if d > b:
#     f = d - b
#     e = c - a
# else:
#     f = d + 60 - b
#     e = c - 1 - a
# print(f"{e} {f}")

# a,b = map(int,input().split())
# c = a * 10 + b
# num = c // 19
# print(num)

# a,b,c = map(int,input().split())
# d = a * 0.2 +b * 0.3 + c * 0.5
# print(int(d))

