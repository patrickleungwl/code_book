class Solution:
    def is_palin(self, s: str) -> bool:
        # bab is a Palin
        # a is a Palin
        # aa is a Palin
        # aaa is a Palin
        result = False
        rev_str = s[::-1]
        if s == rev_str:
            result = True
        return result

    def longestPalindromeBruteForce(self, s: str) -> str:
        longest = ''
        # we keep looking for a reverse- palindome
        # if it's a palindrome, keep the string
        # if it's not a palindrome, shift the starting point over by 1
        #  and repeat search

        for left_idx in range(0, len(s)+1):
            for right_idx in range(left_idx+1, len(s)+1):
                test = s[left_idx:right_idx]
                if self.is_palin(test):
                    if len(test) > len(longest):
                        longest = test

        return longest

    def palin_btwn_middle(self, st: str, i: int) -> str:
        # sabbak
        # if we are at b, we check b+1
        length = 0
        result = st[i]
        while True:
            left = i-length
            right = i+length+2
            if left < 0 or right > len(st):
                break
            test = st[left:right]
            if self.is_palin(test):
                length += 1
                result = test
            else:
                break
        return result

    def palin_middle(self, st: str, i: int) -> str:
        # zracecarx
        length = 1
        result = st[i]
        while True:
            left = i-length
            right = i+length+1
            if left < 0 or right > len(st):
                break
            test = st[left:right]
            if self.is_palin(test):
                length += 1
                result = test
            else:
                break
        return result

    def longestPalindrome(self, s: str) -> str:

        # sabbak
        # sracecark

        longest = ''
        slen = len(s)
        # let's step through the string
        # and look for palindromes
        for i in range(0, slen):
            lg1 = self.palin_btwn_middle(s, i)
            lg2 = self.palin_middle(s, i)
            if len(lg1) > len(longest):
                longest = lg1
            if len(lg2) > len(longest):
                longest = lg2
        return longest


def test_palin():
    s = Solution()
    assert s.is_palin('bab')
    assert not s.is_palin('babad')
    assert s.palin_middle('sabbak', 0) == 's'
    assert s.palin_middle('sabbak', 1) == 'a'
    assert s.palin_middle('zracecarx', 3) == 'c'
    assert s.palin_middle('zracecarx', 4) == 'racecar'
    assert s.palin_middle('racecarx', 3) == 'racecar'
    assert s.palin_middle('zracecar', 4) == 'racecar'
    assert s.palin_btwn_middle('sabbad', 2) == 'abba'
    assert s.palin_btwn_middle('abbad', 1) == 'abba'
    assert s.palin_btwn_middle('abbad', 0) == 'a'
    assert s.palin_btwn_middle('sabba', 2) == 'abba'
    assert s.longestPalindrome('zracecarx') == 'racecar'
    assert s.longestPalindrome('zracecarxabc') == 'racecar'
    assert s.longestPalindrome('z') == 'z'
    assert s.longestPalindrome('za') == 'z'
    assert s.longestPalindrome('cbbd') == 'bb'
