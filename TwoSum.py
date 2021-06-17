class Solution(object):

    def twoSum(self, nums, target):
        lis = []
        for id, num in enumerate(nums):
            if (target - num) in nums[id+1:]:
                lis.append(id)
                lis.append(nums[id+1:].index(target - num)+id+1)
                break
        return lis


s=Solution()
arr = input("")

nums = [int(n) for n in arr.split()]

target=int(input())
id=s.twoSum(nums,target)
print(id)