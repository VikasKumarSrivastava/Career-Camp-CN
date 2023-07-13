# Write a recursive function to convert a given string into the number it represents. That is input will be a numeric string that contains only numbers, you need to convert the string into corresponding integer and return the answer.
# Input format :
# Numeric string S (string, Eg. "1234")
# Output format :
# Corresponding integer N (int, Eg. 1234)


def string_int(str):
    if len(str) ==1:
        return ord(str)-ord('0')
    a=ord(str[0])-ord('0') 
    smallAns = string_int(str[1:])
    return (a*10**(len(str)-1))+smallAns


str =input()
print(string_int(str))
