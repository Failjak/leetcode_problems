from test_cases import test_cases
from collections import defaultdict

# 1876. Substrings of Size Three with Distinct Character
# https://leetcode.com/problems/substrings-of-size-three-with-distinct-characters/


class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        slen = len(s)
        count = 0

        if slen < 3:
            return count

        l, r = 0, 2
        while r < slen:
            if len(set(s[l:r + 1])) == 3:
                count += 1
            l += 1
            r += 1

        return count

    def countGoodSubstringsWithStates(self, s: str, sub_len: int = 3) -> int:
        slen = len(s)
        state = dict()
        count = 0

        r = l = 0
        while r < slen:
            if state.get(s[r]) is not None:
                state[s[r]] += 1 
            else:
                state[s[r]] = 1

            if (r - l + 1) == sub_len:
                if len(state) == sub_len:
                    count += 1
                state[s[l]] -= 1
                if not state[s[l]]:
                    state.pop(s[l])
                l += 1
            r += 1

        return count


test_cases(
    func=Solution().countGoodSubstringsWithStates,
    # func=Solution().countGoodSubstrings,
    keyses=['s', 'sub_len'],
    params=[
        ("xyzzaz", 6),
        ("aababcabc", 3),
    ],
    answers=[0, 4]
)
