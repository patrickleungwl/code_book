"""
Given a roman numeral, convert it to an integer.

Roman numerals are represented by seven different symbols: I, V, X, L, C, D
and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

800 = DCCC
900 = CM
990 = CMXC
910 = CMX


For example, 2 is written as II in Roman numeral, just two one's added
together. 12 is written as XII, which is simply X + II. The number 27
is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right.
However, the numeral for four is not IIII. Instead, the number four is
written as IV. Because the one is before the five we subtract it making
four. The same principle applies to the number nine, which is written as IX.
There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.

"""


class Solution:
    def romanToInt(self, s: str) -> int:

        total = 0
        i = -1
        # let's read from left to right
        # and keep a running total
        while True:
            i += 1
            if i >= len(s):
                break
            c = s[i]
            if c == 'M':
                total += 1000
                continue
            if c == 'C':
                # if next char is D or M, then this is a -100
                if i+1 < len(s):
                    nc = s[i+1]
                    if nc == 'D' or nc == 'M':
                        total -= 100
                        continue
                total += 100
                continue
            if c == 'D':
                total += 500
                continue
            if c == 'L':
                total += 50
                continue
            if c == 'X':
                # if next char is C or L, then this is a -10
                if i+1 < len(s):
                    nc = s[i+1]
                    if nc == 'C' or nc == 'L':
                        total -= 10
                        continue
                total += 10
                continue
            if c == 'V':
                total += 5
                continue
            if c == 'I':
                # if next char is V or X, then this is a -1
                if i+1 < len(s):
                    nc = s[i+1]
                    if nc == 'V' or nc == 'X':
                        total -= 1
                        continue
                total += 1
                continue
        return total


def test_roman_to_int():
    s = Solution()
    assert s.romanToInt('M') == 1000
    assert s.romanToInt('MM') == 2000
    assert s.romanToInt('MMM') == 3000
    assert s.romanToInt('CM') == 900
    assert s.romanToInt('DCCC') == 800
    assert s.romanToInt('DCC') == 700
    assert s.romanToInt('DC') == 600
    assert s.romanToInt('D') == 500
    assert s.romanToInt('CD') == 400
    assert s.romanToInt('CCC') == 300

    assert s.romanToInt('III') == 3
    assert s.romanToInt('IV') == 4
    assert s.romanToInt('IX') == 9
    assert s.romanToInt('LVIII') == 58
    assert s.romanToInt('MCMXCIV') == 1994


s = Solution()
print(s.romanToInt('MM'))
