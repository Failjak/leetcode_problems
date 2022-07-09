from typing import List


from test_cases import test_cases

# 121. Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = prices[0]
        max_price = 0
        profit = 0
        max_profit = 0

        for i in range(1, len(prices)):
            price = prices[i]

            if price < min_price:
                min_price = max_price = price
            elif price > max_price:
                max_price = price
            
            profit = max_price - min_price
            if profit > max_profit:
                max_profit = profit

        return max_profit


test_cases(
    func=Solution().maxProfit,
    keyses=['prices'],
    params=[
        ([7,1,5,3,6,4], ),
        ([7,6,4,3,1], ),
        ([2,4,1], )
    ],
    answers=[5, 0, 3]
)