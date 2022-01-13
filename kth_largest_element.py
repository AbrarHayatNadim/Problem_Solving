arr = [4,2,9,7,5,6,7,1,3]
k = 4

#first Solution

def kth_largest(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)



#2nd Solution


def kth_largest_sorted(arr,k):
    n = len(arr)
    arr.sort()
    return arr[n-k]

#print(kth_largest_sorted(arr, k))

#Third Solution

import heapq

def kth_largest_heap(arr, k):
    arr = [-elem for elem in arr]
    heapq.heapify(arr)
    for i  in range (k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr) 

    