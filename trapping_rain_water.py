from typing import List

from test_cases import test_cases


# 42. Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/submissions/


class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        prev = curr = 0
        tmp_volume = 0
        while curr < len(height):
            if height[prev] > height[curr]:
                tmp_volume += height[prev] - height[curr]
            elif height[prev] <= height[curr]:
                volume += tmp_volume
                tmp_volume = 0
                prev = curr
            curr += 1

        if tmp_volume != 0:
            border = prev
            prev = curr = len(height) - 1
            tmp_volume = 0
            while curr > border:
                if height[prev] > height[curr]:
                    tmp_volume += height[prev] - height[curr]
                elif height[prev] <= height[curr]:
                    volume += tmp_volume
                    tmp_volume = 0
                    prev = curr
                curr -= 1

        return volume


test_cases(
    func=Solution().trap,
    keyses=['height'],
    params=[
        ([4, 1, 2, 3, 4],),
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1],),
        ([4, 2, 0, 3, 2, 5],),
    ],
    answers=[6, 6, 9]
)
