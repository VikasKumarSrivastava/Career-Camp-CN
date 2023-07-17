# Given two string s and t, write a function to check if s contains all characters of t (in the same order as they are in string t).
# Return true or false.
# Do it recursively.
# E.g. : s = “abchjsgsuohhdhyrikkknddg” contains all characters of t=”coding” in the same order. So function will return true.
# Input Format :
# Line 1 : String s
# Line 2 : String t
# Output Format :
# true or false

def solve(s,t,a_id,b_id):
    if (b_id==len(t)):
        return True
    if (a_id==len(s)):
        return False
    if (s[a_id]==t[b_id]):
        return solve(s,t,a_id+1,b_id+1);
    else:
        return solve(s,t,a_id+1,b_id)

def contains(s,t):
    #Implement This Function Here
    return solve(s,t,0,0)
    
s = input()
t = input()

ans = contains(s,t)
if ans is True:
    print('true')
else:
    print('false')
