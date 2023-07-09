# Given a string, compute recursively a new string where all 'x' chars have been removed.
def removeX(string): 
    if len(string) ==0:
        return string
    smallerOutput = removeX(string[1:])
    if string[0]=='x':
        return ''+smallerOutput
    else:
        return string[0]+smallerOutput

  # Main
string = input()
print(removeX(string))

input: axbx
output: ab
