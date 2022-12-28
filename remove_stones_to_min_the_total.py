from queue import PriorityQueue
from typing import List

from test_cases import test_cases


# 1962. Remove Stones to Minimize the Total
# https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        # time: O(nlog)
        # space: O(n)
        sum = 0
        q = PriorityQueue()
        for pile in piles:
            sum -= pile
            q.put(-pile)

        for _ in range(k):
            num = -q.get()
            new_num = num - num // 2
            sum += num // 2
            q.put(-new_num)

        return -sum


test_cases(
    func=Solution().minStoneSum,
    keyses=['piles', 'k'],
    params=[
        ([5, 4, 9], 2),
    ],
    answers=[12]
)
