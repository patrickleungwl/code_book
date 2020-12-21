#import pytest as py
#import unittest

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


    def test_string_slice(self, s: str):
        s='zabaijk'
        print(s[0:1])
        print(s[0:2])
        print(s[0:3])
        print(s[1:1+1])
        print(s[1:2+1])
        print(s[1:3+1])

        l=len(s)-1
        print(s[l:l-1:-1])
        print(s[l:l-2:-1])
        print(s[l:l-3:-1])
                

    def palin_middle(self, s: str, i: int) -> str:
        # sabbak
        length = 1
        result = s[i]
        while True:
            left = i-length
            right = i+length
            if left < 0 or right > len(s):
                break
            test = s[left:right]
            if self.is_palin(test):
                length+=1
                result = test
            else:
                break
        return result


    def longestPalindrome(self, s: str) -> str:

        # sabbak
        # sracecark

        longest = ''
        slen = len(s)-1
        # let's step through the string
        # and look for palindromes
            

        return longest



def test_palin():
    s = Solution()
    assert s.is_palin('bab')
    assert s.is_palin('babad') == False
    assert s.palin_middle('sabbak',0) == 's'
    assert s.palin_middle('sabbak',1) == 'a'
    assert s.palin_middle('sabbak',2) == 'abba'
