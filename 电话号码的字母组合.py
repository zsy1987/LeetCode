class Solution(object):
    def letterCombinations(self, digits):
        if len(digits)==0:
            return []
        list=["abc",'def','ghi','jkl','mno','pqrs','tuv','wxyz']
        res=[]
        def backtrack(con,digit):
            if len(digit)==0:
                res.append(con)
            else:
                for i in list[int(digit[0]) - 2]:
                    backtrack(con+i,digit[1:])
        backtrack('',digits)
        return res
s=Solution()
print(s.letterCombinations("2"))
#递归，回溯