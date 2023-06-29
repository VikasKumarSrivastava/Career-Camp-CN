# For a given two-dimensional integer array/list of size (N x M), you need to find out which row or column has the largest 
# sum(sum of all the elements in a row/column) 
# amongst all the rows and columns.
# If there are more than one rows/columns with maximum sum, 
# consider the row/column that comes first. And if ith row and jth column has the same largest sum, consider the ith row as answer.
# If there doesn't exist a sum at all then print "row 0 -2147483648", where -2147483648 or -2^31 is the smallest value for the range of Integer.
# Sample Input 1:
# 1
# 3 2
# 6 9 
# 8 5 
# 9 2 
# Sample Output 1:
# column 0 23
from sys import stdin
MIN_VALUE = -2147483648
        
def findLargest(arr, nRows, mCols):
    #Your code goes here
    isRow = True
    largestSum = MIN_VALUE
    num = 0
    for i in range(nRows):
        rowSum = 0
        for j in range(mCols):
            rowSum += arr[i][j]
        if rowSum > largestSum:
            largestSum = rowSum
            num = i
    for j in range(mCols):
        colSum = 0
        for i in range(nRows):
            colSum += arr[i][j]
        if colSum > largestSum:
            largestSum = colSum
            num = j
            isRow = False
    if isRow:
        print("row "+str(num)+" "+str(largestSum))
    else:
        print("column "+str(num)+" "+str(largestSum))
