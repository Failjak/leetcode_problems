import enum
from typing import List

from test_cases import test_cases

# 448. Find All Numbers Disappeared in an Array


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        """
        # v1
        mem: O(n)
        compl: O(n)
        """
        # n = len(nums)
        # res = [0 for _ in range(n)]

        # for num in nums:
        #     res[num - 1] = num

        # return [i + 1 for i, n in enumerate(res) if i != n -  1 ]


        """
        # v2
        mem: O(1)
        compl: O(n)
        """
        n = len(nums)
        i = 0
        while i < n:
            ind = nums[i] - 1
            if nums[ind] != nums[i]:
                nums[ind], nums[i] = nums[i], nums[ind]
            else:
                i += 1
        
        return [i + 1 for i in range(n) if nums[i] != i + 1]


test_cases(
    func=Solution().findDisappearedNumbers,
    cases=[
        # ([4,3,2,7,8,2,3,1], [5, 6]),
        # ([1, 1], [2]),
        ([5,4,6,7,9,3,10,9,5,6], [1,2,8]),
        ([9,9,4,10,8,5,2,2,7,7], [1, 3, 6])
    ]
)