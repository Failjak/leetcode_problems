from typing import List

from test_cases import test_cases


# 4. Median of Two Sorted Arrays
# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    # here used way with merging
    def findMedianSortedArraysWithMerge(self, nums1: List[int], nums2: List[int]) -> float:
        # mem: O(n1 + n2)
        # compl: O(n + k)
        res = []

        nums1_len = len(nums1)
        nums2_len = len(nums2)

        first_ind = sec_ind = 0
        while first_ind < nums1_len and sec_ind < nums2_len:
            if nums1[first_ind] < nums2[sec_ind]:
                res.append(nums1[first_ind])
                first_ind += 1
            else:
                res.append(nums2[sec_ind])
                sec_ind += 1

        if first_ind < nums1_len:
            while first_ind < nums1_len:
                res.append(nums1[first_ind])
                first_ind += 1

        elif sec_ind < nums2_len:
            while sec_ind < nums2_len:
                res.append(nums2[sec_ind])
                sec_ind += 1

        num_len = nums1_len + nums2_len
        if num_len % 2:
            return res[num_len // 2]
        else:
            return (res[num_len // 2 - 1] + res[num_len // 2]) / 2

    def findMedianSortedArrays(self, _nums1: List[int], _nums2: List[int]):
        nums_len = len(_nums1) + len(_nums2)

        half_nums_len = nums_len // 2
        if half_nums_len < len(_nums1) and _nums1[half_nums_len] < _nums2[0]:
            return _nums1[half_nums_len] if nums_len % 2 else (_nums1[half_nums_len - 1] + _nums1[half_nums_len]) / 2
        if half_nums_len < len(_nums2) and _nums2[half_nums_len] < _nums1[0]:
            return _nums2[half_nums_len] if nums_len % 2 else (_nums2[half_nums_len - 1] + _nums2[half_nums_len]) / 2

        # case for even nums len
        if not nums_len % 2:

            start1 = 0
            end1 = len(_nums1)
            while start1 < end1:
                curr1 = (start1 + end1) // 2

                start2, end2 = 0, len(_nums2)
                while start2 < end2:
                    curr2 = (start2 + end2) // 2

                    if _nums1[curr1] <= _nums2[curr2]:
                        end2 = curr2 - 1
                    else:
                        start2 = curr2 + 1

                tmp_len = curr1 + start2 + 2
                if tmp_len == nums_len // 2:
                    return (max(_nums1[curr1], _nums2[start2]) + min(_nums1[curr1 + 1], _nums2[start2 + 1])) / 2
                elif tmp_len > nums_len // 2:
                    end1 = curr1 - 1
                elif tmp_len < nums_len // 2:
                    start1 = curr1 + 1
            return (_nums1[end1] + _nums2[curr2]) / 2

        else:
            return "HUI"


test_cases(
    func=Solution().findMedianSortedArrays,
    keyses=['_nums1', '_nums2'],
    params=[
        # ([1, 3], [2]),
        # ([1, 2], [3, 4]), -> 2.5
        ([11, 13, 17], [1, 5, 10]),
        ([1, 5, 10, 22, 33], [2, 13, 17, 25, 44]),
        ([1, 4, 6, 10, 12], [2, 7, 13, 20, 21]),
        ([1, 2, 3, 4], [5, 6])
    ],
    answers=[10.5, 15, 8.5, 3.5]
)

# 1, 2, 5
# 5, 6

# [5, 7, 10, 14, 18, 20]
# [1, 3, 4, 8, 9, 13, 19, 22]
# target - 9.5
