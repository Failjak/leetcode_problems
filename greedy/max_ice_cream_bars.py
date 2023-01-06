import heapq
from typing import List

from test_cases import test_cases


# 1833. Maximum Ice Cream Bars
# https://leetcode.com/problems/maximum-ice-cream-bars/

def max_ice_cream(costs: List[int], coins: int) -> int:
    bar_prices = []
    left_coins, bars = coins, 0

    for cost in costs:
        if left_coins < 0:
            return bars
        if cost > coins:
            continue

        if not bar_prices:
            bars += 1
            left_coins -= cost
            heapq.heappush(bar_prices, -cost)

        elif left_coins >= cost:
            bars += 1
            left_coins -= cost
            heapq.heappush(bar_prices, -cost)

        elif left_coins < cost:
            max_bar_price = -heapq.heappop(bar_prices)
            if max_bar_price > cost:
                left_coins = left_coins + max_bar_price - cost
                heapq.heappush(bar_prices, -cost)
            else:
                heapq.heappush(bar_prices, -max_bar_price)

    return bars


test_cases(
    func=max_ice_cream,
    keyses=["costs", "coins"],
    params=[
        ([1, 3, 2, 4, 1], 7),
        ([10, 6, 8, 7, 7, 8], 5),
        ([1, 6, 3, 1, 2, 5], 20),
        ([10, 6, 8, 7, 7, 8], 12),
    ],
    answers=[4, 0, 6, 1],
)
