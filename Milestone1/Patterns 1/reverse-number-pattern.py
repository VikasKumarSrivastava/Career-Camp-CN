# Pattern for N = 4
# 1
# 21
# 321
# 4321

n = int(input())
i=1
while i <= n:
    j=1
    p=i
    while j <= i:
        print(p,end='')
        j= j+1
        p=p-1
    print()
    i = i+1
