a={"apple","abc",23}

type(a)

'abc' in a

21 in a

for v in a:
    print(v)

len(a)

a.add("temp")

b={'abc','ghi'}

a.update(b)

a.remove('temp')

a.remove('rrr')

a.discard(23)

a.discard('rrr')

a.pop()


a={1,2,3,4}
b={3,4,5,6}

a.intersection(b)

a.union(b)

a.difference(b)

b.difference(a)

a.symmetric_difference(b)

a.intersection_update(b)

a.difference_update(b)

a.symmetric_difference_update(b)

c={3,4}

a.issubset(b)

a.issubset(c)

c.issubset(a)

a.issuperset(c)

a.isdisjoint(b)

d={7,8}

a.isdisjoint(d)
