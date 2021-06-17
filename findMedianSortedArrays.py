class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()

        if len(nums1)%2==0:
            return (nums1[int(len(nums1)/2)]+nums1[int(len(nums1)/2-1)])/2
        else:
            return  nums1[int((len(nums1)-1)/2)]

s=Solution()
arr1 = input("")

l1 = [int(n) for n in arr1.split()]

arr2 = input("")

l2 = [int(n) for n in arr2.split()]
result=s.findMedianSortedArrays(l1,l2)
print(result)