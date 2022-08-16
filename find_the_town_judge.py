from collections import defaultdict
from typing import List

from test_cases import test_cases


# 997. Find the Town Judge
# https://leetcode.com/problems/find-the-town-judge/


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        peoples = defaultdict(int)

        for t in trust:
            peoples[t[0]] -= 1
            peoples[t[1]] += 1

        for i in range(1, n + 1):
            if peoples[i] == n - 1:
                return i
        return -1


test_cases(
    func=Solution().findJudge,
    params=[
        (2, [[1, 2]]),
        (3, [[1, 3], [2, 3]]),
        (3, [[1, 3], [2, 3], [3, 1]]),
    ],
    answers=[
        2,
        3,
        -1,
    ],
    keyses=['n', 'trust']
)
