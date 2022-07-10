from typing import List

# 303. Range Sum Query - Immutable
# https://leetcode.com/problems/range-sum-query-immutable/


class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.cache = {}
    
    def sumRange(self, left: int, right: int) -> int:
        left_sum = right_sum = 0
        
        if not self.cache.get(left):
            self.cache[left] = sum(self.nums[:left + 1])
        left_sum = self.cache[left]
        
        if not self.cache.get(right):
            self.cache[right] = sum(self.nums[:right + 1])
        right_sum = self.cache[right]
        
        return right_sum - left_sum + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
