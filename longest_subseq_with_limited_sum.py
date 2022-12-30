from typing import List

from test_cases import test_cases


# 2389. Longest Subsequence With Limited Sum
# https://leetcode.com/problems/longest-subsequence-with-limited-sum/


class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        sums = [0]
        for num in sorted(nums):
            sums.append(num + sums[-1])

        def bs(to_find: int, nums: List[int]) -> int:
            if to_find >= nums[-1]:
                return len(nums) - 1

            l, r = 0, len(nums) - 1
            while l <= r:
                midd = (l + r) // 2
                if nums[midd] > to_find:
                    r = midd - 1
                elif nums[midd] < to_find:
                    l = midd + 1
                elif nums[midd] == to_find:
                    return midd
            return l - 1

        return [bs(q, sums) for q in queries]


test_cases(
    func=Solution().answerQueries,
    keyses=['nums', 'queries'],
    params=[
        ([4, 5, 2, 1], [3, 10, 21],),
        ([2, 3, 4, 5], [1])
    ],
    answers=[[2, 3, 4], [0]]
)
