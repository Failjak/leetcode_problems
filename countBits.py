from typing import List, Optional
from test_cases import test_cases


# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/


class Solution:
    def decimal_to_binar(self, n: int) -> str:
        bin = ''
        while n:
            bin += f'{n % 2}'
            n //= 2
        return bin[::-1]    

    def countBits_v1(self, n: int) -> List[int]:
        """
        mem: O(n)
        compl: O(n log n)
        """
        res = []
        for i in range(n + 1):
            res.append(self.decimal_to_binar(i).count('1'))
        return res

    def solve(self, n: int, memo: Optional[List] = None) -> int:
        memo = memo if memo else [0 for _ in range(n + 1)] 

        if (n == 0): return 0
        if (n == 1): return 1

        if n in memo: return memo[n]

        if (n % 2 == 0): 
            memo[n] = self.solve(n // 2, memo)
            return self.solve(n // 2, memo)
        else:
            memo[n] = self.solve(n // 2, memo) + 1
            return self.solve(n // 2, memo) + 1

    def countBits(self, n: int) -> List[int]:
        res = []

        for i in range(n + 1):
            res.append(self.solve(i))

        return res          

# 15 -> 1111
# -> 4

# 14 -> 1110
# -> 3

# 13 -> 1101
# -> 3

# 12 -> 1100
# -> 2

# 11 -> 1011
# -> 3

# 10 -> 1010
# -> 2

# 9 -> 1001
# -> 2

# 8 ->  1000
# -> 1


# 7 -> 111
# -> 3

# 6 -> 110
# -> 2

# 5 -> 101
# -> 2

# 4 -> 100
# -> 1


# 3 -> 11
# -> 2

# 2 -> 10
# -> 1 


# 1 -> 1
# -> 1 

# 0 -> 0
# -> 0


"""
6 -> (3) -> 2
3 -> (1) -> 1 + 1
1 -> 1

9 -> (4) -> 1 + 1 -> 2
4 -> (2) -> (1)
2 -> (1) -> 1

"""

test_cases(
    # func=Solution().countBits_v1,
    func=Solution().countBits,
    keyses=['n'],
    params=[
        (2, ),
        (5, )
    ],
    answers=[[0,1,1], [0,1,1,2,1,2]]
)