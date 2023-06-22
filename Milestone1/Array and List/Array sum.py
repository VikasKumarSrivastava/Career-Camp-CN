# Given an array of length N, you need to find and print the sum of all elements of the array.

# Read input as sepcified in the question
# Print output as specified in the question

n = int(input())
li=[int(x) for x in input().split()]
sum = 0 
for ele in li:
    sum = sum + ele

print(sum)
