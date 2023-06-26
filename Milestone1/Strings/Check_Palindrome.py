# Given a string, determine if it is a palindrome, considering only alphanumeric characters.
# Sample Input 1 :
# abcdcba
# Sample Output 1 :
# true 
# Sample Input 2:
# coding
# Sample Output 2:
# false

inputsStr = input()
i = 0
j = len(inputsStr) - 1
l_flag = True
while i < j:
    if inputsStr[i] == inputsStr[j]:
        i=i+1
        j=j-1
    else:
        l_flag = False
        break
        
if l_flag:
    print('true')
else:
    print('false')
