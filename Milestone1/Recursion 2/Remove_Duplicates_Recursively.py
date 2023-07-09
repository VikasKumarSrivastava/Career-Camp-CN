# # Given a string S, remove consecutive duplicates from it recursively.
# Sample Input 1 :
# aabccba
# Sample Output 1 :
# abcba

def removeConsecutiveDuplicates(string):
    # Please add your code here
    if len(string)==0 or len(string)==1:
        return string
    if string[0] !=string[1]:
        return string[0] + removeConsecutiveDuplicates(string[1:])
    return removeConsecutiveDuplicates(string[1:])

# Main
string = input().strip()
print(removeConsecutiveDuplicates(string))
