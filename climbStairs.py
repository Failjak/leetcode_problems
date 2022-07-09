from test_cases import test_cases

class Solution:
    def climbStairs(self, n: int) -> int:
        """
        mem: O(1)
        compl: O(n)
        """

        one, two = 1, 1
        for _ in range(n - 1):
            tmp = one
            one += two
            two = tmp

        return one

    def graphClimgStairs(self, n: int) -> int:
        i = 0
        d1, d2 = 1, 2
        queue = {0: [1, 2]}

        for i in range(n):
            neibs = queue.get(i, 0)
            for neib in neibs:
                queue[neib] = neib + d1, neib + d2

"""
1: 1
2: 2

3: 3
111
12
21

4: 5
1111
112
121
211
22

5: 8
11111
1112
1121
1211
2111
122
212
221

6: 13
111111
11112
11121
11211
12111
21111
1122
1212
2112
2121
2211
222
1221

"""


test_cases(
    func=Solution().climbStairs,
    keyses=['n'],
    params=[
        (2, ),
        (3, ),
        (5, ),
    ],
    answers=[2, 3, 8]
)
