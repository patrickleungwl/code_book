"""
Given a 32-bit signed integer, reverse digits of an integer.

Note:
Assume we are dealing with an environment that could only store integers within
the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this
problem, assume that your function returns 0 when the reversed integer
overflows.

ex1
Input: x = 123
Output: 321

ex2
Input: x = -123
Output: -321

ex3
Input: x = 120
Output: 21

ex4
Input: x = 0
Output: 0

Let us handle this problem like a stack.
We push each digit into the stack
and then we pull them out.

How to peel off each digit?
from the left?

123 % 10 = 3
123 / 10 =12

321
3   nn = 3
2   nn = 3*10+2 = 32
1   nn = 32*10+1 = 321
"""


class Solution:
    def reverse(self, x: int) -> int:
        nn = 0
        is_neg = False
        if x < 0:
            is_neg = True
            x = x * -1

        while x > 0:
            digit = x % 10
            nn = nn * 10 + digit
            x = int(x / 10)

        if is_neg:
            nn = -1 * nn

        if nn >= pow(2, 31)-1 or nn < -1 * pow(2, 31):
            nn = 0

        return nn


def test_reverse():
    s = Solution()
    assert s.reverse(123) == 321
    assert s.reverse(-123) == -321
    assert s.reverse(120) == 21
    assert s.reverse(0) == 0
    assert s.reverse(1534236469) == 0
    assert s.reverse(1563847412) == 0


s = Solution()
s.reverse(1563847412)
