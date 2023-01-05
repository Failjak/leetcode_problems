from typing import List

from test_cases import test_cases


# 452. Minimum Number of Arrows to Burst Balloons
# https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

def findMinArrowShots(points: List[List[int]]) -> int:
    points.sort(key=lambda p: p[1])
    arrows = 1
    _, curr_end = points[0]

    for (start, end) in points[1:]:
        if curr_end < start:
            arrows += 1
            curr_end = end

    return arrows


test_cases(
    func=findMinArrowShots,
    keyses=["points"],
    params=[
        ([[3, 9], [7, 12], [3, 8], [6, 8], [9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]],),
    ],
    answers=[
        2,
    ]
)
