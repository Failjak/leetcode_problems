from typing import List
from test_cases import test_cases


# 268. Missing Number

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        """
        memory: O(1)
        compl: O(2n) -> O(n)
        """
        # v.1
        # n = len(nums)
        # n_sum= sum(nums)
        # return sum(range(n + 1)) - n_sum

        # v.2
        n = len(nums)
        return n * (n + 1) // 2 - sum(nums)


test_cases(
    func=Solution().missingNumber,
    keyses=['nums'],
    params=(
        ([3,0,1], ),
        ([0,1], ),
        ([9,6,4,2,3,5,7,0,1], )
    ),
    answers=[2, 2, 8]
)