n = int(input("请输入一个整数n: "))#输入

matrix = [[0] * n for i in range(n)]#制表

shang = 0   #规定变量
zuo = 0
xia = n-1
you = n-1
num = 1

while num <= n**2 :
    for i in range(zuo,you+1):
        matrix[shang][i] = num
        num += 1
    shang += 1
    for i in range(shang,you+1):
        matrix[i][you] = num
        num +=1
    you -= 1
    for i in range(you,zuo-1,-1):
        matrix[xia][i] = num
        num += 1
    xia -= 1
    for i in range(xia,shang-1,-1):
        matrix[i][zuo] = num
        num += 1
    zuo += 1
for a in matrix:
        print(' '.join(map(str,a)))
