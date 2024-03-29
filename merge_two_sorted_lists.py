from typing import List

from test_cases import test_cases


class Solution:
    # def mergeTwoSortedLists(self, nums1: List[int], nums2: List[int]) -> List[int]:
    #     res = []
    #
    #     first_ind = sec_ind = 0
    #     while first_ind < len(nums1) and sec_ind < len(nums2):
    #         if nums1[first_ind] < nums2[sec_ind]:
    #             res.append(nums1[first_ind])
    #             first_ind += 1
    #         else:
    #             res.append(nums2[sec_ind])
    #             sec_ind += 1
    #
    #     if first_ind < len(nums1):
    #         while first_ind < len(nums1):
    #             res.append(nums1[first_ind])
    #             first_ind += 1
    #
    #     elif sec_ind < len(nums2):
    #         while sec_ind < len(nums2):
    #             res.append(nums2[sec_ind])
    #             sec_ind += 1
    #
    #     return res

    def mergeTwoSortedLists(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums = []
        ind1 = ind2 = 0
        while ind1 < len(nums1) and ind2 < len(nums2):
            if nums1[ind1] < nums2[ind2]:
                nums.append(nums1[ind1])
                ind1 += 1
            else:
                nums.append(nums2[ind2])
                ind2 += 1

        while ind1 < len(nums1):
            nums.append(nums1[ind1])
            ind1 += 1

        while ind2 < len(nums2):
            nums.append(nums2[ind2])
            ind2 += 1

        return nums



test_cases(
    func=Solution().mergeTwoSortedLists,
    keyses=['nums1', 'nums2'],
    params=[
        ([1, 3], [2]),
        ([1, 4], [2, 3]),
        ([0, 1, 12, 44], [2, 3, 7, 23, 100]),
    ],
    answers=[
        [1, 2, 3],
        [1, 2, 3, 4],
        [0, 1, 2, 3, 7, 12, 23, 44, 100]
    ]
)
