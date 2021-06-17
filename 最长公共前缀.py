class Solution(object):
    def longestCommonPrefix(self, strs):
        k,t=0,0
        if len(strs)==1:
            return strs[0]
        else:

            while True:
                if k<min(len(i) for i in strs):
                    temp=strs[0][k]
                    for s in strs:
                        if s[k]==temp:
                            temp=s[k]
                        else:
                            t=1
                            break
                    if t==1:
                        break
                    k = k + 1
                else:
                    break
            if k==0:
                return ''
            else:
                return strs[0][:k]
s=Solution()
print(s.longestCommonPrefix(["ab","a"]))



#改过来过去 这个题真的吐了
#原来还可以横向扫描 牛的 一个一个比
#还可以横向分治、还可以纵向二分 太强了