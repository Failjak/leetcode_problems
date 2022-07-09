from typing import List


from test_cases import test_cases

# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        tmp = []
        for i, n in enumerate(prices[:-1]):
            to_sell = max(prices[i + 1:])
            tmp.append(to_sell - n)

        res = max(tmp)
        return res if res >= 0 else 0



test_cases(
    func=Solution().maxProfit,
    keyses=['prices'],
    params=[
        ([7,1,5,3,6,4], ),
        ([7,6,4,3,1], )
    ],
    answers=[5, 0]
)