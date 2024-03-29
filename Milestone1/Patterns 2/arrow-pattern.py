# Print the following pattern for the given number of rows.
# Assume N is always odd.
# Note : There is space after every star.
# Pattern for N = 7
# *
#  * *
#    * * *
#      * * * *
#    * * *
#  * *
# *
## Read input as specified in the question.
## Print output as specified in the question.
n = int(input())
m = n // 2 + 1 #1st half
i = 1

while i <= m:
    sp = 1
    while sp < i:
        print(" ", end = "")
        sp+=1        
    j = i
    c = 1
    while j >= i and c <= i:
        print("* ",end = "")
        j+=2
        c+=1       
    print()
    i+=1
   
i = m - 1   #2nd half
while i >= 1: 
    sp = 1
    while sp < i:
            print(" ", end = "")
            sp+=1
            
    j = i
    c = 1
    while j >= 1 and c <= i:
        print("* ",end = "")
        j+=2
        c+=1
        
    print()
    i-=1
