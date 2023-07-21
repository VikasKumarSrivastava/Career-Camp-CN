# You have been given an integer array/list(ARR) and a number X. Find and return the total number of pairs in the array/list which sum to X.
def pairSum(arr, n, x) :
    #Your code goes here
    # if n ==0:
    #     return 0
    # count= 0
    # for i in range(0,n-1):
    #     for j in range(i+1,n):
    #         if arr[i] + arr[j] == num:
    #             count= count + 1
    # return count

    d = {}
    count = 0
    for i in range(n):
        if x - arr[i] in d:
            count += d[x - arr[i]]
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1
    return count
