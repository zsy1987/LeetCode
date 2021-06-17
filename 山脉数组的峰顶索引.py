class Solution:
    def peakIndexInMountainArray(self, arr):
        left,res=0,1
        right=len(arr)-2
        while left<right:
            mid=(right+left)//2
            if arr[mid]>arr[mid+1]:
                right=mid-1
                res=mid
            else:
                left=mid+1
        return  res

s=Solution()
print(s.peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))

#二分查找，
#python如何实现归并排序？