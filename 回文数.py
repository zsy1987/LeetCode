class Solution(object):
    def isPalindrome(self, x):
        if x<0:
            temp=False
        else:
            st=str(x)
            st2=st[::-1]
            if st==st2:
                temp=True
            else:
                temp=False
        return temp