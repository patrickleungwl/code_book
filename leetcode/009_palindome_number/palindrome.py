"""
Determine whether an integer is a palindrome. An integer is a palindrome
when it reads the same backward as forward.

Follow up: Could you solve it without converting the integer to a string?

ex1
Input: x = 121
Output: true

ex2
Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it
becomes 121-. Therefore it is not a palindrome.

ex3
Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

ex4
Input: x = -101
Output: false

"""


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False

        # check that the leftmost digit is the same as the rightmost digit
        # 1221
        # 121
        #
        # we can put the digits into a vector
        # and then scan the vector from left and from right
        # and compare the digits
        v = []
        while x > 0:
            digit = x % 10    # this grabs the right-most digit
            v.append(digit)
            x = int(x / 10)

        # 1 2 2 1
        # 1 2 1
        left = 0
        right = len(v)-1
        is_palin = True
        while True:
            if left >= right:
                break
            left_digit = v[left]
            right_digit = v[right]
            if left_digit != right_digit:
                is_palin = False
                break
            left += 1
            right -= 1

        return is_palin


def test_palindrome():
    s = Solution()
    assert s.isPalindrome(121) is True
    assert s.isPalindrome(-121) is False
    assert s.isPalindrome(10) is False
    assert s.isPalindrome(-101) is False
