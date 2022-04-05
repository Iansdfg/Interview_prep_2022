from lintcode import (
    ListNode,
)

"""
Definition of ListNode:
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: the first list
    @param l2: the second list
    @return: the sum list of l1 and l2 
    """
    def add_lists(self, l1, l2):
        # write your code here
        carry = 0
        res = []
        dummy = ListNode(-1)
        tail = dummy
        while l1 or l2 or carry: 
            ans = carry
            carry = 0

            if l1:
                ans += l1.val
                l1 = l1.next

            if l2:
                ans += l2.val
                l2 = l2.next

            if ans >= 10:
                carry = ans//10
                ans = ans % 10

            print(ans, carry)
            tail.next = ListNode(ans)
            tail = tail.next

        return dummy.next




