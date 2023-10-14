def rotate(nums, k):
    for i in range(k):
        nums.insert(0,nums.pop())
    return nums
nums=list(map(int,input().split()))
k=int(input())
print(rotate(nums,k))
