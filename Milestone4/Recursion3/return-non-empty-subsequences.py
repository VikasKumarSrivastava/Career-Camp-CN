# Problem statement:
# https://www.codingninjas.com/studio/problems/subsequences-of-string_985087?leftPanelTab=0
def subsequencesHelper(str,index,temp,ans):
    if index == len(str):
        if len(temp)!=0:
            ans.append(temp)
        return
    #exclude
    subsequencesHelper(str,index+1,temp,ans)

    temp +=str[index]
    #include 
    subsequencesHelper(str,index+1,temp,ans)


def subsequences(str):

    #n = len(str)
    ans =[]
    temp=""
    subsequencesHelper(str,0,temp,ans)

    return ans

# TC: O(N^2)
# SC : O(N) recursive stack + O(N^2) as there can be n(n-1)/2 subsequences possible
#     ~O(N^2)
