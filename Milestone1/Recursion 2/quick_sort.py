# QuickSort is a sorting algorithm based on the Divide and Conquer algorithm that picks an element as a pivot
# and partitions the given array around the picked pivot by placing the pivot in its correct position in the sorted array.
# Working of Quick Sort:
  # The key process in quickSort is a partition(). The target of partitions is to place the pivot (any element can be chosen to be a pivot) 
  # at its correct position in the sorted array and put all smaller elements to the left of the pivot, 
  # and all greater elements to the right of the pivot.
  # Partition is done recursively on each side of the pivot after the pivot is placed in its correct position 
  # and this finally sorts the array.
# Time Complexity:
  # Best Case: \omega (N * log N)
  # Average Case: \Theta (N * logN)
  # Worst Case: O(N2)
# Auxiliary Space: O(log(N))
# It is not a stable sort, meaning that if two elements have the same key, their relative order will not be preserved 
# in the sorted output in case of quick sort, 
# because here we are swapping elements according to the pivot’s position (without considering their original positions).
# For more details visit: https://www.geeksforgeeks.org/quick-sort/
# Important article : https://www.geeksforgeeks.org/why-quick-sort-preferred-for-arrays-and-merge-sort-for-linked-lists/
