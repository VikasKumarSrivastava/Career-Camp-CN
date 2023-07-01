def sumUnique(li):
  s= set() #creating an empty set
  for i in li:
    s.add(i)
  sum = 0
  for i in s:
    sum = sum + i
  return sum

sumUnique([1,2,3,4,3,4,2,1,5,5])
    
