from test_cases import test_cases
from typing import List


# 217. Contains Duplicate

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """
        memory: O(n)
        compl: O(n)
        """
        vals = set([])

        for num in nums:
            if num in vals:
                return True
            vals.add(num)

        return False            



test_cases(
    func=Solution().containsDuplicate,
    keyses=['nums'],
    params=[
        ([1,2,3,1], ),
        ([1,2,3,4], ),
        ([1,1,1,3,3,4,3,2,4,2], )
    ],
    answers=[True, False, True]
)
