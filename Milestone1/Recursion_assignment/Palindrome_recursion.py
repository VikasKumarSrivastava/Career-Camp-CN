# Check whether a given String 'S' is a palindrome using recursion.
# Return true or false.
def solve(string:str,si,ei):
    if si==ei:
        return True
    if string[si]!=string[ei]:
        return False
    if si < ei + 1:
        return solve(string,si+1,ei-1)
    return True

def isPalindrome(string: str) -> bool:
    if len(string) == 0:
        return True
    # ans = solve(string,0,len(string)-1)
    return solve(string,0,len(string)-1)
    
