# def rotate(nums, k,search):
#     for i in range(k):
#         nums.insert(0,nums.pop())
#     print(nums)
#     return nums.index(search)

def search( nums, target):
    """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
    start=0
    end=len(nums)-1
    mid=(start+end)/2
    while 1:
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            end=mid-1
        else:
            start=mid+1
    else:
        return -1
            

nums=list(map(int,input().split()))

# k=int(input())
search=int(input())
print(search(nums,search))
