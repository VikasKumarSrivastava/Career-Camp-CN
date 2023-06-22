#linear search
n = int(input())
target = 7
isFound = False
li = [int(x) for x in input().split()]
for i in range(len(li)):
    if li[i] == target:
        isFound=True
        print(i)
        break
if isFound is False:
    print(-1)
