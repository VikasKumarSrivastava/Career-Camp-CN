# You are given N, and for a given N x N chessboard, find a way to place N queens such that no queen can attack any other queen on the chess board. A queen can be killed when it lies in the same row, or same column, or the same diagonal of any of the other queens.
# You have to print all such configurations.
# Note : Don't print anything if there isn't any valid configuration.
# Constraints :
# 1<=N<=10
# Sample Input 1:
# 4
# Sample Output 1 :
# 0 1 0 0 0 0 0 1 1 0 0 0 0 0 1 0 
# 0 0 1 0 1 0 0 0 0 0 0 1 0 1 0 0 
# Time complexity: O(N!): The first queen has N placements,
# the second queen must not be in the same column as the first as well as at an oblique angle, 
# so the second queen has N-1 possibilities, and so on, with a time complexity of O(N!).
# Spatial Complexity: O(N): Need to use arrays to save information.

    
def isSafe(row,col,board,n):
    #vertical
    i=row-1
    while i>=0:
        if board[i][col] == 1:
            return False
        i-=1
    #diagonal left
    i=row-1
    j=col-1
    while i>=0 and j>=0:
        if board[i][j]==1:
            return False
        i-=1
        j-=1
    #diagonal right
    i=row-1
    j=col+1
    while i>=0 and j<n:
        if board[i][j]==1:
            return False
        i-=1
        j+=1
    return True
def nQueenHelper(row,n,board):
    if row==n:
        for i in range(n):
            for j in range(n):
                print(board[i][j],end=' ')
        print()
        return
    
    for col in range(n):
        if isSafe(row,col,board,n):
            board[row][col]=1
            nQueenHelper(row+1,n,board)
            #backtracking step
            board[row][col]=0
    return
def nQueen(n):
    #Implement Your Code Here
    board =[[0 for j in range(n)]for i in range(n)]
    nQueenHelper(0,n,board)


n = int(input())
nQueen(n)

