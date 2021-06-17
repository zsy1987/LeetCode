class Solution(object):
    def lengthOfLongestSubstring(self, s):
        hashmap={}
        lis=[0,0]
        for idx,c in enumerate(s):
             if c in hashmap.keys():
                 lis.append(idx-hashmap[c])
             hashmap[c] = idx
        return max(lis)

s=Solution()
t = str(input())
re=s.lengthOfLongestSubstring(t)
print(s)
