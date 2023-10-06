# def merge(l,start,mid,end):
    # i=start
    # j=mid
    # k=start
    # while i<mid and j<end:
    #     if l[i]<l[j]:
    #         l[k]=l[i]
    #         i+=1
    #     else:
    #         l[k]=l[j]
    #         j+=1
    #     k+=1
    # while i<mid:
    #     l[k]=l[i]
    #     i+=1
    #     k+=1
    # while j<end:
    #     l[k]=l[j]
    #     j+=1
    #     k+=1
    # return l
# def mergeSort(l,start,end):
#     if start<end:
#         return l
#     mid=len(n)//2
#     mergeSort(n,start,mid)
#     mergeSort(n,mid+1,end)
#     ml=merge(l,start,mid,end)
    # return ml



# def merge(left,right):
#     res=[]
#     i=j=0
#     while i<len(left) and j<len(right):
#         if left[i]<right[j]:
#             res.append(left[i])
#             i+=1
#         else:
#             res.append(right[j])
#             j+=1
#     # if i==len(left):
#         # for i in range(j,len(right)-1):
#         #     res.appedn(right[j])
#             # j+=1  
#     # if j==len(right):
#         # for i in range(i,len(left)-1):
#         #     res.append(left[i])
#         #     i+=1
#     res.extend(left[i:])
#     res.extend(right[j:])
    
#     return res

# def mergeSort(l):
#     if len(l)>1:
#         mid=len(l)//2
#         left=l[:mid]
#         right=l[mid:]
#         left=mergeSort(left)
#         right=mergeSort(right)
#         mergeSort(left)
#         mergeSort(right)
#         print(left,right)
#         merged_list=merge(left,right)
#         return merged_list
#     return l



def mergeSort(l):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        left=mergeSort(left)
        right=mergeSort(right)
        mergeSort(left)
        mergeSort(right)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1  
    return l

n=[x for x in input().split()]
print(mergeSort(n))