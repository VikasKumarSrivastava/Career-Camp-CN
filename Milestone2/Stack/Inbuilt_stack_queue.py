#inbuilt stack as list
s=[1,2,3]
s.append(4)
s.append(5)
print(s.pop())
print(s.pop())

#inbuilt queue
import queue
q=queue.Queue()
q.put(1)
q.put(2)
q.put(3)
q.put(4)
while not q.empty():
    print(q.get())
  
#queue as Stack
import queue
q=queue.LifoQueue()
q.put(1)
q.put(2)
q.put(3)
while not q.empty():
    print(q.get())
