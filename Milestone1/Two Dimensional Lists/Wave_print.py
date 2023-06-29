#For a given two-dimensional integer array/list of size (N x M), print the array/list in a sine wave order, i.e, print the first column top to bottom, 
# next column bottom to top and so on.
# Sample Input 1:
# 1
# 3 4 
# 1  2  3  4 
# 5  6  7  8 
# 9 10 11 12
# Sample Output 1:
# 1 5 9 10 6 2 3 7 11 12 8 4

from sys import stdin

def wavePrint(mat, nRows, mCols):
    #Your code goes here
    for j in range(mCols):
        if j%2 == 0:
            for i in range(nRows):           
                print(mat[i][j],end=" ")
        else:
            for i in range(nRows-1,-1,-1):           
                print(mat[i][j],end=" ")
