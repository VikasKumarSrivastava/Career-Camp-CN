# Given a string, find and return all the possible permutations of the input string.
# Note :
# The order of permutations are not important.
# Sample Input :
# abc
# Sample Output :
# abc
# acb
# bac
# bca
# cab
# cba
   # Time Complexity: O(N! * log(N!))
   #  Space complexity: O(N * N!)
    
   #  Where N is the length of the given string.
def genPermutation(str,l,r,ans):
    if l==r:
        ans.append(str)
        return
    
    for i in range(l,r+1):
        str = list(str)
        str[l],str[i] = str[i],str[l]

        str = "".join(str)
        genPermutation(str,l+1,r,ans)

        #backtrack
        str =list(str)
        str[l],str[i]=str[i],str[l]
        str="".join(str)

def permutations(string):
    #Implement Your Code Here
    ans =[]
    l = 0
    r = len(string)-1

    genPermutation(string,l,r,ans)
    ans.sort()
    return ans

string = input()
ans = permutations(string)
for s in ans:
    print(s)
