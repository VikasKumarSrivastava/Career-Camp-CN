# For a given expression in the form of a string, 
# find the minimum number of brackets that can be reversed in order to make the expression balanced. The expression will only contain curly brackets.
# If the expression can't be balanced, return -1.
# Example:
# Expression: {{{{
# If we reverse the second and the fourth opening brackets, the whole expression will get balanced. 
#   Since we have to reverse two brackets to make the expression balanced, the expected output will be 2.

# Expression: {{{
# In this example, even if we reverse the last opening bracket, we would be left with the 
#   first opening bracket and hence will not be able to make the expression balanced and the output will be -1.
# Sample Input 1:
# {{{
# Sample Output 1:
# -1
# Sample Input 2:
# {{{{}}
# Sample Output 2:
# 1
from sys import stdin

def isEmpty(st):
    return len(st) ==0
def top(st):
    return st[len(st)-1]
def countBracketReversals(inputString) :
    # Your code goes here
    if len(inputString)%2!=0:
        return -1
    count=0
    st =[]
    for i in range(len(inputString)):
        if inputString[i]=='{':
            st.append(inputString[i])
        else:
            if not isEmpty(st) and top(st)=='{':
                st.pop()
            else:
                st.append(inputString[i])
    while not isEmpty(st):
        ele1= top(st)
        st.pop()
        ele2=top(st)
        st.pop()
        if ele1==ele2:
            count+=1
        else:
            count+=2
    return count

#main
print(countBracketReversals(stdin.readline().strip()))
