class Solution(object):

    def iszero(self,nums):
        T=0
        for i in nums:
            if i!=0:
                T=1
        if T==0:
            return True
        else:
            return False
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if self.iszero(nums) and len(nums)>=3:
            return [[0,0,0]]
        elif len(nums)<3:
            return []
        elif len(nums)==3:
            if sum(nums)==0:
                return [nums]
            else:
                return []
        else:

            res=[]
            a=[]
            b=[]

            for i in nums:
                if i<0:
                    a.append(-i)
                else:
                    b.append(i)
            b.append(999999)
            a.append(111111)
            a.sort()
            b.sort()


            for q,i in enumerate(a):
                if i==a[q-1]:
                    continue
                j, k = 0, len(b) - 1
                while j<k:
                    if b[j]+b[k]<i:
                        j = j + 1
                    elif b[j]+b[k]>i:
                        k = k - 1
                    else:
                        re=[b[j],b[k],-i]

                        res.append(re)
                        j = j + 1
                        k = k - 1



            for q,i in enumerate(b):
                if i==b[q-1]:
                    continue
                j, k = 0, len(a) - 1
                while j < k:
                    if a[j] + a[k] < i:
                        j = j + 1
                    elif a[j] + a[k] > i:
                        k = k - 1
                    else:
                        re=[-a[j], -a[k], i]

                        res.append(re)
                        j = j + 1
                        k=k-1

            return res



s=Solution()
print(s.threeSum([-2,0,1,1,2]))
#剔重 心态崩了