from typing import List, Set

from test_cases import test_cases


# 797. All Paths From Source to Target
# https://leetcode.com/problems/all-paths-from-source-to-target/


class Solution:

    def find_path(self, parent, target, graph, visited: Set, path: List, paths: List):
        visited.add(parent)
        path.append(parent)

        if parent == target:
            paths.append(path.copy())
        else:
            for v in graph[parent]:
                if not v in visited:
                    self.find_path(v, target, graph, visited, path, paths)

        path.pop()
        visited.remove(parent)


    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        target = len(graph) - 1
        visited = set()
        self.find_path(0, target, graph, visited, [], paths)

        return paths

test_cases(
    func=Solution().allPathsSourceTarget,
    keyses=['graph'],
    params=[
        ([[1, 2], [3], [3], []],),
        # ([[1, 4, 5], [2], [3], [], [6], [6], []], )
    ],
    answers=[[[0, 1, 3], [0, 2, 3]]]
)
