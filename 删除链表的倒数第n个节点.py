
class ListNode:
    def __init__(self, val=0, next=None):
       self.val = val
       self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
       res=ListNode(0,head)
       first=head
       second=res
       while n:
           # first.

           first=first.next
           n=n-1

       while first:

           first=first.next
           second=second.next

       second.next=second.next.next
       return res.next

h = ListNode(1,2)
s=Solution()

s.removeNthFromEnd(h,2)
