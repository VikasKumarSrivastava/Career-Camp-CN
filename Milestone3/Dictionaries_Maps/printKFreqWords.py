def printKFreqWords(s,k):
    words=s.split()
    d={}
    for w in words:
        d[w]=d.get(w,0)+1
    for w in d:
        if d[w]==k:
            print(w)

s="this is a word string having many many word"
k=2
printKFreqWords(s,k)
