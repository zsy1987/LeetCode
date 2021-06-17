class Solution(object):
    def threeSumClosest(self, nums, target):
        nums.sort()
        # print(nums)
        n = len(nums)
        res = float("inf")  # Python中可以用如下方式表示正负无穷：float("inf"), float("-inf")
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:#妙啊
                continue
            left = i + 1
            right = n - 1
            while left < right:
                cur = nums[i] + nums[left] + nums[right]
                if cur == target: return target
                if abs(res - target) > abs(cur - target):
                    res = cur
                if cur > target:
                    right -= 1
                elif cur < target:
                    left += 1
        return res