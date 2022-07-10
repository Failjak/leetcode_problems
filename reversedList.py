from typing import List, Optional

from test_cases import test_cases

# 206. Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # a -> b -> c -> d -> None
    # d -> c -> b -> a -> None
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        
        previous = None
        curr = head

        while True:
            # b | c | d | 
            tmp_curr = curr.next

            # a -> None | b -> a | c -> b
            curr.next = previous

            # a | b | c
            previous = curr

            if not tmp_curr:
                break

            # b | c | d
            curr = tmp_curr

        return curr


def generate_link_list(nums: List[int]):
    main = ListNode(nums[0])
    head = main
    for num in nums[1:]:
        head.next = ListNode(num)
        head = head.next

    return main


test_cases(
    func=Solution().reverseList,
    keyses=['head'],
    params=[
        (generate_link_list([1, 2, 3, 4, 5]), ),
    ],
    answers=['-']
)
