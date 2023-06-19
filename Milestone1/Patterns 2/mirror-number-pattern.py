# Code : Mirror Number Pattern
# Send Feedback
# Print the following pattern for the given N number of rows.
# Pattern for N = 4
# ...1
# ..12
# .123
# 1234
# The dots represent spaces.

n = int(input())
i =1
while i <= n:
    j=1
    while j <= n-i:
        print(" ",end="")
        j=j+1
    k=1
    while j <= n:
        print(k,end="")
        k=k+1
        j=j+1
    print()
    i=i+1
