import unittest


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # on every iteration, we keep track of the current substring
        # that is our longest string
        # when we reach the second a, we start new string
        # from b, making new string bcda
        #

        longest = 0
        cur_str = ''

        for idx in range(0,len(s)):
            c = s[idx]
            if c in cur_str:
                # if find character exists already
                # we make our str shift over by 1 char
                tidx = cur_str.index(c)
                cur_str = cur_str[tidx+1:]                

            cur_str += c
            longest = max(longest, len(cur_str))

        return longest



    def lengthOfLongestSubstringOld(self, s: str) -> int:

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
        self.assertEqual(2,s.lengthOfLongestSubstring('au'))
        self.assertEqual(3,s.lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1,s.lengthOfLongestSubstring('bbbb'))
        self.assertEqual(3,s.lengthOfLongestSubstring('pwwkew'))
        self.assertEqual(0,s.lengthOfLongestSubstring(''))
        self.assertEqual(1,s.lengthOfLongestSubstring(' '))
        self.assertEqual(3,s.lengthOfLongestSubstring('dvdf'))


unittest.main()

