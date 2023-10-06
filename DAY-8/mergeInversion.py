def mergeSort(l,inversion):
    if len(l)>1:
        mid=len(l)//2
        left=l[:mid]
        right=l[mid:]
        li=mergeSort(left,inversion)
        ri=mergeSort(right,inversion)
        mergeSort(left,inversion)
        mergeSort(right,inversion)
        i=j=k=0
        while i<len(left) and j<len(right):
            if left[i]<=right[j]:
                l[k]=left[i]
                i+=1
                k+=1
            else:
                l[k]=right[j]
                j+=1
                k+=1
                inversion+=len(left)-i
        while i<len(left):
            l[k]=left[i]
            i+=1
            k+=1
        while j<len(right):
            l[k]=right[j]
            j+=1
            k+=1  
        return li+ri+inversion
    return 0
n=[x for x in input().split()]
print(mergeSort(n,0))