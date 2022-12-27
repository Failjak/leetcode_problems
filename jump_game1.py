from typing import List

from test_cases import test_cases


# 55 Jump Game
# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        i = len(nums) - 2
        min_ind_to_solve = len(nums) - 1

        while i >= 0:
            len_to_end = min_ind_to_solve - i
            steps = nums[i]

            if steps >= len_to_end:
                min_ind_to_solve = i

            i -= 1

        return not min_ind_to_solve


test_cases(
    func=Solution().canJump,
    keyses=['nums'],
    params=[
        ([1, 2, 3, 0, 4, 5, 2],),
        ([2, 3, 1, 1, 4],),
        ([3, 2, 1, 0, 4],)
    ],
    answers=[True, True, False]
)
