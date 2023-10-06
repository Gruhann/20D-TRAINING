# quick sort
def partition(n,start,end):
    pivot=n[end]
    i=start-1
    for j in range(start,end):
        if n[j]<pivot:
            i+=1
            n[i],n[j]=n[j],n[i]
    n[i+1],n[end]=n[end],n[i+1]
    return i+1

def quickSort(n,start,end):
    if start<end:
       pivot=partition(n,start,end)
       quickSort(n,start,pivot-1)
       quickSort(n,pivot+1,end) 
    return n 
# mid=len(n//2)
# quickSort(n[:mid])
# quickSort(n[mid+1:])
#above logic for merge sort  
#complexity of partition function is n
#complexity of quickSort depends on depth of recursion tree
#best and avg case n(log(n))
#worst case n^2
n=[x for x in input().split()]
print(quickSort(n,0,len(n)-1))

#USING DIFFERENT LISTS
# def quickSort(arr):
#     if len(arr)<=1: 
#         return arr
#     pivot=arr[len(arr)//2]
#     left=[x for x in arr if x<pivot]
#     mid=[x for x in arr if x==pivot]
#     right=[x for x in arr if x>pivot]
   
#     return quickSort(left)+mid+quickSort(right)
# n=[x for x in input().split()]
# print(quickSort(n))
  