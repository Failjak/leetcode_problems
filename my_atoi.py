from test_cases import test_cases


class Solution:
    def myAtoi(self, s: str) -> int:
        minus_restrict = -2147483648
        plus_restrict = 2147483647
        sign = ""
        num = ""
        prev_c = ""

        for c in s:
            if c == " ":
                if num or sign:
                    break
            elif c.isalpha():
                break
            elif c == ".":
                break
            elif c in "-+":
                if prev_c.isnumeric():
                    break
                if sign:
                    break
                sign = c
            else:
                num += c
            prev_c = c

        int_num = int(sign + num) if num else 0

        if int_num < minus_restrict:
            return minus_restrict
        if int_num > plus_restrict:
            return plus_restrict

        return int_num


test_cases(
    func=Solution().myAtoi,
    keyses=['s'],
    params=[
        ("4193 with words",),
        ("words and 987",),
        ("   -42",)
    ],
    answers=[4193, 0, -42]
)
