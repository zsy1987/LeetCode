# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        p1=l1
        p2=l2
        ex=1
        sum=0
        while p1 is not None:
            sum=sum+p1.val*ex
            ex=ex*10
            p1=p1.next
        ex=1
        while p2 is not None:
            sum=sum+p2.val*ex
            ex=ex*10
            p2=p2.next
        ssum=str(sum)
        re=ListNode(0)
        p3=re
        for s in ssum[::-1]:
            p3.next=ListNode(int(s))
            p3=p3.next
        return re.next

s=Solution()
arr1 = input("")

l1 = [int(n) for n in arr1.split()]

arr2 = input("")

l2 = [int(n) for n in arr2.split()]
result=s.addTwoNumbers(l1,l2)
print(result)