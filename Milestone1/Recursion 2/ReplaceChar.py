def replaceChar(s,a,b):
    if len(s)==0:
        return s
    smallerOutput=replaceChar(s[1:],a,b)
    if s[0]==a:
        return b+smallerOutput
    else:
        return s[0] + smallerOutput

replaceChar('vikassakiv','s','z')
output: 'vikazzakiv'
