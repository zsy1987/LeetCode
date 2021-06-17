class Solution(object):
    def maxArea(self, height):
        maxv=0
        i=0
        j=len(height)-1
        while i!=j:
            volume =  min(height[i],height[j])*(j-i)
            if height[i]<height[j]:
                i=i+1
            else:
                j=j-1
            if maxv<volume:
               maxv=volume
        return  maxv

s=Solution()
print(s.maxArea([1,8,6,2,5,4,8,3,7]))