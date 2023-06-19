# Print the following pattern for the given number of rows.
# Pattern for N = 5
#  1    2   3    4   5
#  11   12  13   14  15
#  21   22  23   24  25
#  16   17  18   19  20
#  6    7    8   9   10
n = int(input())

if n%2 == 0:
    m = n//2
else:
    m = n//2+1
    
for i in range(1, m+1, 1):
    for j in range(1, n+1, 1):
        print(2*n*(i-1)+j, end ='')
        print(' ',end = '') 
    print()
    
r = n - m
for i in range(r, 0, -1):
    for j in range(1, n+1, 1):
        print((2*i-1)*n + j, end ='')
        print(' ', end ='')
    print()
