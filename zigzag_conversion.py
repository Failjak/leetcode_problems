from test_cases import test_cases


# 6. Zigzag Conversion
# https://leetcode.com/problems/zigzag-conversion/

class Solution:
    def convert(self, s: str, num_rows: int) -> str:
        if num_rows == 1: return s
        rows = [""] * num_rows
        row_num = 0
        go_down = False
        for c in s:
            rows[row_num] += c
            if not row_num or row_num == num_rows - 1: go_down = not go_down
            row_num += 1 if go_down else -1

        return "".join(rows)


test_cases(
    func=Solution().convert,
    keyses=['s', 'num_rows'],
    params=[
        ("PAYPALISHIRING", 3),
        ("PAYPALISHIRING", 4),
        ("A", 1),
    ],
    answers=["PAHNAPLSIIGYIR", "PINALSIGYAHRPI", "A"]
)
