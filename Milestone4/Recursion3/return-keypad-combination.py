# Given an integer n, using phone keypad find out and return all the possible strings that can be made using digits of input n.
# Sample Input:
# 23
# Sample Output:
# ad
# ae
# af
# bd
# be
# bf
# cd
# ce
# cf
def getString(n):
    if n==2:
        return 'abc'
    if n==3:
        return 'def'
    if n==4:
        return 'ghi'
    if n==5:
        return 'jkl'
    if n==6:
        return 'mno'
    if n==7:
        return 'pqrs'
    if n==8:
        return 'tuv'
    if n==9:
        return 'wxyz'
    return ''

def keypad(n):
    #Implement Your Code Here
    if n ==0:
        output=[]
        output.append("")
        return output

    smallerInteger = n//10
    lastDigit= n%10

    smallerOutput = keypad(smallerInteger)
    optionforlastdigit = getString(lastDigit)
    output2=[]

    for s in smallerOutput:
        for c in optionforlastdigit:
            option = s+c
            output2.append(option)

    return output2

n = int(input())
ans = keypad(n)
for s in ans:
    print(s)
