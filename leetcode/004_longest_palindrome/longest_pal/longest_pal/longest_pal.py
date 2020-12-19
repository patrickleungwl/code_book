
import unittest

class Solution:
    def isPalin(self, s: str) -> bool:
        # bab is a Palin
        # a is a Palin
        # aa is a Palin
        # aaa is a Palin
        
        result = False
        rev_str = s[::-1]
        if s == rev_str:
            result = True
        
        return result



    def longestPalindrome(self, s: str) -> str:
        longest = ''

        # we keep looking for a reverse- palindome
        # if it's a palindrome, keep the string
        # if it's not a palindrome, shift the starting point over by 1
        #  and repeat search

        for left_idx in range(0, len(s)+1):
            for right_idx in range(left_idx+1, len(s)+1):
                test = s[left_idx:right_idx]
                print('%s' % test)


        return ''


class mytest(unittest.TestCase):
    def testPalin(self):
        s = Solution()
        self.assertTrue(s.isPalin('bab'))
        self.assertFalse(s.isPalin('babad'))

        #self.assertEqual(s.longestPalindrome('babad'),'bab')
        #self.assertEqual(s.longestPalindrome('cbbd'),'bb')
        #self.assertEqual(s.longestPalindrome('a'),'a')
        #self.assertEqual(s.longestPalindrome('ac'),'a')


unittest.main()

