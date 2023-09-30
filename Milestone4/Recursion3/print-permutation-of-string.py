Given a string, find and print all the possible permutations of the input string.
Sample Input :
abc
Sample Output :
abc
acb
bac
bca
cab
cba
def printPermutationsHelper(string,ans):
    if len(string)==0:
        print(ans)

        return

    for i in range(len(string)):
        printPermutationsHelper(string[:i] + string[i+1:],ans+string[i])
        
def printPermutations(string):
    #Implement Your Code Here
    printPermutationsHelper(string,"")

string = input()
printPermutations(string)





