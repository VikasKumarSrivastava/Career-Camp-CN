## Read input as specified in the question.
## Print output as specified in the question.

# Given a string (lets say of length n), print all the subsequences of the given string.
# Subsequences contain all the strings of length varying from 0 to n. But the order of characters should remain same as in the input string.
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
def printsubSequences(str,output):

    if len(str) ==0:
        print(output)
        return

    #exclude
    printsubSequences(str[1:],output)

    #include
    printsubSequences(str[1:],output+str[0])


str= input()
printsubSequences(str,"")
