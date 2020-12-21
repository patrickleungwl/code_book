"""
Given an array of integers nums and an integer target, return indices
of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you
may not use the same element twice.

You can return the answer in any order.

Ex1:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Ex2:
Input: nums = [3, 2, 4], target = 6
Output: [1, 2]

Ex3:
Input: nums = [3, 3], target = 6
Output: [0, 1]

Strategy
Think it is best to precache each number and its location in the first pass.
Then with the second pass, we immediately know if there is a complement
for each target-digit.

"""
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        number_location = {}
        for i, n in enumerate(nums):
            what_we_want = target - n
            if what_we_want in number_location:
                return [number_location[what_we_want], i]
            number_location[n] = i
        return []


def test_twosum():
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [0, 1]
    assert s.twoSum([3, 2, 4], 6) == [1, 2]
    assert s.twoSum([3, 3], 6) == [0, 1]
