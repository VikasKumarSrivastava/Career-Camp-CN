# Code : Star Pattern
# Send Feedback
# Print the following pattern
# Pattern for N = 4
# ...*
# ..***
# .*****
# *******
# Hint
# As taught in the video, you just have to modify the code so that instead of printing numbers, it should output stars ('*').
# The dots represent spaces.


n =int (input())
i = 1

while i <= n:
    j =1
    while j <= n-i:
        print(" ",end="")
        j=j+1
    while j<=n:
        print('*',end="")
        j=j+1
    k=1
    while k <= i-1:
        print('*',end="")
        k=k+1
    print()
    i = i+1
