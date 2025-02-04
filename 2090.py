#某医院进行一项研究，想知道某项疾病是否与年龄有关。
# 因此对以往的诊断记录进行整理，统计 0-18 、 19-35 、 36-60、 61 及以上 这四个年龄段的患者人数占总患者人数的比例。
from array import ArrayType

nums = int(input())     #表示总患者人数。
num = map(int,input().split())    #代表这N个患者就诊时的年龄。
a = 0
b = 0
c = 0
d = 0
for i in num:
    if 0 <= i <= 18 :
        a = a + 1
    else:
        a = a
    if 19 <= i <= 35 :
        b = b + 1
    else:
        b = b
    if 36 <= i <= 60 :
        c = c +1
    else:
        c = c
    if i >= 61:
        d = d + 1
    else:
        d = d
A = a/nums
B = b/nums
C = c/nums
D = d/nums
print(f"{A:.2%}\n"
      f"{B:.2%}\n"
      f"{C:.2%}\n"
      f"{D:.2%}")
