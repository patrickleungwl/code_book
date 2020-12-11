import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # look for string from left to right
        # keep track of all chars found
        # and also length
        # if already found, record length- is it the longest?
        # reset found map and continue searching

        longest = 0
        max = len(s)

        for start in range(0, max):
            found_chars = {}
            length = 0

            for idx in range(start, max):
                c = s[idx]

                # abcdab
                # start = a
                # idx = b

                # we should always update length count
                length += 1

                # if new char, store it
                # if seen before, we break out now
                if c not in found_chars:
                    found_chars[c] = 1
                    if length > longest:
                        longest = length
                else:
                    break

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

