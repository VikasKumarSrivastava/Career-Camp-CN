# Given a string (let's say of length n), return all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain the same as in the input string.
# Note: The order of subsequences are not important.
# Sample Input:
# abc
# Sample Output:
# "" (the double quotes just signifies an empty string, don't worry about the quotes)
# c 
# b 
# bc 
# a 
# ac 
# ab 
# abc 
def subsequences(string):
    #Implement Your Code Here
    if len(string) == 0:
        output=[]
        output.append("")
        return output
        
    smallerOutput = subsequences(string[1:])
    output2=[]
    for sub in smallerOutput:
        output2.append(sub)
        output2.append(string[0]+sub)
    return output2

string = input()
ans = subsequences(string)
for ele in ans:
    print(ele)
