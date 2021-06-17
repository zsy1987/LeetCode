class Solution(object):
    def isPalindrome(self, x):
        reverNumber=0
        if x<0 or (x%10==0 and x!=0):
            return False
        else:
            while x>reverNumber:
                reverNumber=reverNumber*10+x%10
                x=x/10
        return x==reverNumber or x==reverNumber/10