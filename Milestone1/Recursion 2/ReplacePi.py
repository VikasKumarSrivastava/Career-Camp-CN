#Replace pi with 3.14 in given string
def replacePi(s):
    if len(s)==0 or len(s)==1:
        return s
    if s[0]=='p'and s[1]=='i':
        smallOutput = replacePi(s[2:])
        return '3.14'+smallOutput
    else:
        smallOutput=replacePi(s[1:])
        return s[0]+smallOutput

input: replacePi('pipippppipiip')
output: '3.143.14ppp3.143.14ip'
