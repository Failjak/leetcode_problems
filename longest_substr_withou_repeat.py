from math import degrees
from test_cases import test_cases


# 3. Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        indexes = {}
        for i in range(len(s)):
            if True:
                pass
            indexes[s[i]] = i


    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     res = 0

    #     def get_str_without_repeat(s, start):
    #         chars = ''

    #         for c in s[start:]:
    #             if c not in chars:
    #                 chars += c
    #             else:
    #                 break
    #         return len(chars)

    #     for i in range(len(s)):
    #         tmp = get_str_without_repeat(s, i)
    #         if tmp > res:
    #             res = tmp

    #     return res


test_cases(
    debug=True,
    func=Solution().lengthOfLongestSubstring,
    keyses=['s'],
    params=[
        ('abcabcbb', ),
        ('bbbbb', ),
        ('pwwkew', )
    ],
    answers=[
        3, 1, 3
    ],
)
