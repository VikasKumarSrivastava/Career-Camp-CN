# You have been given a random integer array/list(ARR) and a number X. Find and return the number of triplets in the array/list which sum to X.
def findTriplet(arr, n, x) :
    #Your code goes here
    #return your answer
    if n ==0:
        return 0
    count= 0
    for i in range(0,n-2):
        for j in range(i+1,n-1):
            for k in range( j+1, n):
                if arr[i] + arr[j]  + arr[k]== x:
                    count= count + 1
    return count
