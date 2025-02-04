n = int(input())
if n <= 0:
    print(0)
    exit()
else:
    nums = list(map(int, input().split()))
    a = max(nums)
    num = 0
    for i in nums:
        if i < a:
            num = num + i
    print(num)
