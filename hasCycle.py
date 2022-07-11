from typing import List, Optional
from test_cases import test_cases

# 141. Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        mem: O(n)
        comp: O(n)
        """
        visited = {}
        while head:
            if head not in visited:
                visited[head] = 1
            else:
                return True
            head = head.next
        return False

    def hasCycle_v1(self, head: Optional[ListNode]) -> bool:
        """
        mem: O(1)
        compl: O(n)
        """
        slow = fast = head
        while 1:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False
