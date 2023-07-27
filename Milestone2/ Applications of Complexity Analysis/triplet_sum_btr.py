# You have been given a random integer array/list(ARR) and a number X. Find and return the triplet(s) in the array/list which sum to X.
from sys import stdin
def pair_sum(arr,si,ei,num):
    numPair =0
    while si<ei:
        if arr[si] +arr[ei] < num:
            si+=1
        elif arr[si]+arr[ei] > num:
            ei-=1
        else:
            ele_at_st = arr[si]
            ele_at_en= arr[ei]
            if ele_at_st ==ele_at_en:
                total = (ei -si) +1
                numPair +=(total*(total-1)//2)
                return numPair
            tsi  = si+1
            tei = ei-1
            while(tsi<=tei) and (arr[tsi]==ele_at_st):
                tsi+=1
            while(tei>=tsi) and (arr[tei]==ele_at_en):
                tei-=1
            total_ele_start = tsi-si
            total_ele_end = ei-tei
            numPair +=total_ele_start * total_ele_end
            si = tsi
            ei=tei
    return numPair
def tripletSum(arr, n, num) :
	#Your code goes here
    arr.sort()
    ans = 0
    for i in range(n):
        pairSumFor= num - arr[i]
        numPairs = pair_sum(arr,i+1,n-1,pairSumFor)

        ans  += numPairs
    return ans


#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(tripletSum(arr, n, num))

    t -= 1
