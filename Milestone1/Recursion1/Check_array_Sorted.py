def solve(arr,si):
    l =len(arr)
    if si==l-1 or si==l:
        return True
    if arr[si] > arr[si+1]:
        return False
    return solve(arr,si+1)

arr =[1,2,4,60,60]
solve(arr,0)
