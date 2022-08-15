import collections
from collections import defaultdict
from typing import List

from test_cases import test_cases


# 721. Accounts Merge
# https://leetcode.com/problems/accounts-merge/


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        graph = collections.defaultdict(set)
        email_to_name = {}

        for account in accounts:
            name = account[0]

            for email in account[1:]:
                graph[email].add(account[1])
                graph[account[1]].add(email)

                email_to_name[email] = name

        visited = {}

        def __visited(n):
            visited[n] = True

            for u in graph[n]:
                if email_to_name.pop(u, None):
                    __visited(u)

        for v in graph:
            if name := email_to_name.pop(v, None):
                __visited(v)
                # print([name, *sorted(visited.keys())])
                yield [name, *visited.keys()]
                visited.clear()


# test_cases(
#     debug=False,
#     func=Solution().accountsMerge,
#     keyses=['accounts', ],
#     params=[
#         ([["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["John", "johnsmith@mail.com", "john00@mail.com"],
#           ["Mary", "mary@mail.com"], ["John", "johnnybravo@mail.com"]],),
#     ],
#     answers=[
#         [["John", "john00@mail.com", "john_newyork@mail.com", "johnsmith@mail.com"], ["Mary", "mary@mail.com"],
#          ["John", "johnnybravo@mail.com"]],
#     ],
# )
