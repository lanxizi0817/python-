n = int(input("样本容量"))
num1 = 0.0
for i in range(n):
    nums = input().split()
    for num in nums:
        num1 = float(num) + num1
a = num1/n
print("%.4f"%a)



n=int(input())
a=input().split()
a=[float(x) for x in a]
zhi = sum(a)/n
print("%.4f"%zhi)