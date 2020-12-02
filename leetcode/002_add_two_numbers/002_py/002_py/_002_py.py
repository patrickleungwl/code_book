
# You are given two non-empty linked lists representing two non-negative integers. 
# The digits are stored in reverse order, and each of their nodes contains a single 
# digit. Add the two numbers and return the sum as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 
# itself.

#Ex 1
#2 .. 4 .. 3
#5 .. 6 .. 4
#7 .. 0 .. 8

#Input: l1 = [2,4,3], l2 = [5,6,4]
#Output: [7,0,8]
#Explanation: 342 + 465 = 807.

#Input: l1 = [0], l2 = [0]
#Output: [0]

#Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
#Output: [8,9,9,9,0,0,0,1]

#The number of nodes in each linked list is in the range [1, 100].
#0 <= Node.val <= 9
#It is guaranteed that the list represents a number that does not have leading zeros.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

#from typing import ListNode

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1_str = ''
        for i in l1:
            num1_str += str(i)
        num1 = int(num1_str)

        num2_str = ''
        for i in l2:
            num2_str += str(i)
        num2 = int(num2_str)

        total = num1 + num2
        return total



list1 = [2,4,3]
list2 = [5,6,4]
s = Solution()
print(s.addTwoNumbers(list1,list2))




        