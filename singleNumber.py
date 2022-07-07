from typing import List
from test_cases import test_cases

# 136. Single Number


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """
        mem: O(1)
        compl: O(n)
        """

        mask = 0
        for num in nums:
            mask ^= num
        return mask


test_cases(
    func=Solution().singleNumber,
    cases=[
        ([2,2,1], 1),
        ([4,1,2,1,2], 4),
        ([1], 1)
    ]
)