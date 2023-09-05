# Given a string S, you need to remove all the duplicates. That means, the output string should contain each character only once. 
# The respective order of characters should remain same, as in the input string.
# Sample Input 1 :
# ababacd
# Sample Output 1 :
# abcd
# Sample Input 2 :
# abcde
# Sample Output 2 :
# abcde
def uniqueChar(s): 
    # Write your code here
    #TC O(N)
    #SC O(N)
    ans=''
    d={}
    for w in s:
        if w not in d:
            ans = ans+w
            d[w]=True
    return ans
# Main 
s=input() 
print(uniqueChar(s))
