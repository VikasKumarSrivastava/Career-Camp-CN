# For a given two-dimensional integer array/list of size (N x M), print it in a spiral form. 
#That is, you need to print in the order followed for every iteration:
# a. First row(left to right)
# b. Last column(top to bottom)
# c. Last row(right to left)
# d. First column(bottom to top)
#  Mind that every element will be printed only once.
# Sample Input 1:
# 1
# 4 4 
# 1 2 3 4 
# 5 6 7 8 
# 9 10 11 12 
# 13 14 15 16
# Sample Output 1:
# 1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10 

from sys import stdin

def spiralPrint(mat, nRows, mCols):
    #Your code goes here

    m =nRows
    n = mCols
    
    k = 0; l = 0

    while (k < m and l < n) : 
        for i in range(l, n) : 
            print(mat[k][i], end = " ") 
              
        k += 1
  
        for i in range(k, m) : 
            print(mat[i][n - 1], end = " ") 
              
        n -= 1
  
        if ( k < m) : 
              
            for i in range(n - 1, (l - 1), -1) : 
                print(mat[m - 1][i], end = " ") 
              
            m -= 1
          
        if (l < n) : 
            for i in range(m - 1, k - 1, -1) : 
                print(mat[i][l], end = " ") 
              
            l += 1
