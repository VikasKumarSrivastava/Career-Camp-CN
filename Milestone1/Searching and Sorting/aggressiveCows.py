# https://www.codingninjas.com/studio/problems/aggressive-cows_1082559?leftPanelTab=0
def canWePlace(stalls,dist,cows):
    cntCows = 1
    last = stalls[0]
    for i in range(1,len(stalls)):
        if stalls[i] - last >= dist:
            cntCows+=1
            last = stalls[i]
        if cntCows>=cows:
            return True
    return False
    
def aggressiveCows(stalls, k):
    # Write your code here.
    stalls.sort()
    n = len(stalls)
    low = 1
    high = stalls[n-1]-stalls[0]
    while low<=high:
        mid = (low+high)//2
        if(canWePlace(stalls,mid,k)==True):
            low = mid+1
        else:
            high = mid - 1
    return high
