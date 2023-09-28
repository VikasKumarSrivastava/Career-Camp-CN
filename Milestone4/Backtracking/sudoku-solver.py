# You are given a 9*9 sudoku board, in which some entries are filled, and others are 0 (0 indicates that the cell is empty).
# You must return true if the Sudoku puzzle can be solved. Else return false.
# Sample Input :
# 9 0 0 0 2 0 7 5 0 
# 6 0 0 0 5 0 0 4 0 
# 0 2 0 4 0 0 0 1 0 
# 2 0 8 0 0 0 0 0 0 
# 0 7 0 5 0 9 0 6 0 
# 0 0 0 0 0 0 4 0 1 
# 0 1 0 0 0 5 0 8 0 
# 0 9 0 0 7 0 0 0 4 
# 0 8 2 0 4 0 0 0 6
# Sample Output :
# true
# Time Complexity
# The input for this problem is a fixed nine-box grid, so it is straightforward to count the actual number of times.

# The first line has no more than nine spaces to be filled with numbers, and since this cannot be repeated, there are 9! ways to do this, and there are nine lines in total, so it takes at most (9!)⁹ times.

# Space complexity
# We have defined three arrays, each with 81 elements, for a total of 3x81=243 elements.

def isSafeColumn(col,n,board):
    for i in range(9):
        if board[i][col]==n:
            return True
    return False
def isSafeRow(row,n,board):
    for j in range(9):
        if board[row][j]==n:
            return True
    return False

def isSafeBox(row,col,n,board):
    for i in range(row,row+3):
        for j in range(col,col+3):
            if board[i][j]==n:
                return True
    return False

def isPossible(row,col,n,board):
    if (isSafeRow(row,n,board)):
        return False
    if (isSafeColumn(col,n,board)):
        return False
    if (isSafeBox(row-(row%3),col-(col%3),n,board)):
        return False
    return True
def solveSudoku(board):
    #Implement Your Code Here
    row=-1
    col=-1
    flag =False
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                row=i
                col=j
                flag = True
                break
        if flag is True:
            break
    if row == -1:
        return True

    for n in range(1,10):
        if isPossible(row,col,n,board):
            board[row][col]=n
            if (solveSudoku(board) is True):
                return True
            #backtracking step
            board[row][col]=0
    return False

board = [[ int(ele) for ele in input().split() ]for i in range(9)]
ans = solveSudoku(board)
if ans is True:
    print('true')
else:
    print('false')
