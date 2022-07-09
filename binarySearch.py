from typing import List


from test_cases import test_cases

class Solution:
    def binarySearch(self, nums: List[int], to_find: int) -> int:
        n = len(nums)
        left, rigth = 0, n - 1

        while left <= rigth:
            midd = (rigth + left) // 2
            if nums[midd] > to_find:
                rigth = midd - 1
            elif nums[midd] < to_find:
                left = midd + 1
            else:
                return midd
        
        return -1



test_cases(
    func=Solution().binarySearch,
    keyses= ['nums', 'to_find'],
    params=[
        ([1, 5, 6, 9, 15, 22, 28], 1),
        ([2, 3, 5, 7, 9, 13, 14, 20, 23], 23),
    ],
    answers = [0, 8]
)