import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # look for string from left to right
        # keep track of all chars found
        # and also length
        # if already found, record length- is it the longest?
        # reset found map and continue searching

        longest = 0
        len_count = 0
        found_chars = {}
        for i in range(0,len(s)):
            c = s[i]
            if c in found_chars:
                if len_count > longest:
                    longest = len_count
                # let's reset
                len_count = 0
                found_chars = {}

            len_count += 1
            found_chars[c] = 1

        if len_count > longest:
            longest = len_count

        return longest


class myTest(unittest.TestCase):

    def test_findLongest(self):
        s = Solution()     
        self.assertEqual(3,s.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1,s.lengthOfLongestSubstring('bbbb'))
        self.assertEqual(3,s.lengthOfLongestSubstring('pwwkew'))
        self.assertEqual(0,s.lengthOfLongestSubstring(''))
        self.assertEqual(1,s.lengthOfLongestSubstring(' '))
        self.assertEqual(3,s.lengthOfLongestSubstring('dvdf'))


unittest.main()

