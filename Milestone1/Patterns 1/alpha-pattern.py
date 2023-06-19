# Print the following pattern for the given N number of rows.
# Pattern for N = 3
#  A
#  BB
#  CCC
n = int(input())

i = 1
while i <= n:
    start_Char = chr(ord('A')+i-1)
    j =1 
    while j <= i:
        charP = chr(ord(start_Char))
        print(charP,end="")
        j = j +1

    print()
    i = i +1
