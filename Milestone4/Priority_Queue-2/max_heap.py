
import heapq
arr=[3,5,7,1,4]
for i in range (0,len(arr)):
  arr[i]=arr[i] * -1
print(arr)
heapq.heapify(arr)
print('after heapifying')
print(arr)
print(-heapq.heappop(arr))
print(arr)
print(-heapq.heappop(arr))
print(arr)
# print(-heapq.heappop(arr))
# print(arr)
heapq.heapreplace(arr,-2)
print(arr)
# print(-heapq.heappop(arr))
# print(arr)
# print(-heapq.heappop(arr))
# print(arr)
