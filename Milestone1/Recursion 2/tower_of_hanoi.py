# Tower of Hanoi is a mathematical puzzle where we have three rods and n disks. The objective of the puzzle is to move all disks from source rod to destination rod using third rod (say auxiliary). The rules are :
# 1) Only one disk can be moved at a time.
# 2) A disk can be moved only if it is on the top of a rod.
# 3) No disk can be placed on the top of a smaller disk.

def towerofhanoi(n, source, aux, dest):
    # Please add your code here
    if n==0:
        return
    if n==1:
        print( source, dest)
        return
    towerofhanoi(n-1,source,dest,aux)
    print(source,dest)
    towerofhanoi(n-1,aux, source,dest)

n=int(input())
towerofhanoi(n, 'a', 'b', 'c')
