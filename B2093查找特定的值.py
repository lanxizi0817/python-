# 在一个序列（下标从0开始）中查找一个给定的值，输出第一次出现的位置。
# 输入格式
# 第一行包含一个正整数n，表示序列中元素个数。1≤n≤10000。
# 第二行包含n 个整数，依次给出序列的每个元素，相邻两个整数之间用单个空格隔开。元素的绝对值不超过10000。
# 第三行包含一个整数x，为需要查找的特定值。x的绝对值不超过 10000。
# 输出格式
# 若序列中存在x，输出x第一次出现的下标； 否则输出 -1。
import sys

n = int(input())     #表示序列中元素个数
if n < 1 or n > 1000:
    sys.exit()
nums = map(int,input().split())   #序列中每个元素
x = int(input())    #需要查找的特定值
for i in nums :
    a = 0
    a = a + 1
    if x==i:
        print(a)
        break
if x != i:
    print(-1)



n = int(input())
nums = input().split()
x = input()
if nums.count(x):
    print(nums.index(x))
else:
    print("-1")
