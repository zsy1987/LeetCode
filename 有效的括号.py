class Solution:
    def isValid(self, s: str) -> bool:
        l=[]
        d={
            ")": "(",
            "]": "[",
            "}": "{",
        }
        for i in s:
            if i in d:
                if not l or l[-1]!=d[i]:
                    return False
                l.pop()
            else:
                l.append(i)
        return not l
