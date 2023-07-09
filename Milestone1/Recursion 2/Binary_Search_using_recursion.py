def binarySearch(a,x,si,ei):
    if si>ei:
        return -1
    mid = (si+ei)//2
    if a[mid] ==x:
        return mid
    elif a[mid] > x:
        return binarySearch(a,x,si,mid-1)
    else:
        return binarySearch(a,x,mid+1,ei)

binarySearch([1,2,3,4,5],1,0,4)
ans => 0
