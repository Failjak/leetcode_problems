from typing import List


from test_cases import test_cases

# 53. Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/


class Solution:

    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum_so_far = curr_max = nums[0]

        for i in range(1, n):
            curr_max = max(nums[i], curr_max + nums[i])
            sum_so_far = max(sum_so_far, curr_max)
        
        return sum_so_far


test_cases(
    func=Solution().maxSubArray,
    keyses=['nums'],
    params=[
        ([-2,1,-3,4,-1,2,1,-5,4], ),
        ([5,4,-1,7,8], ),
        ([-1], )
    ],
    answers=[6, 23, 1]
)
