"""
You are given two non-empty linked lists representing two non-negative
integers. The digits are stored in reverse order,  and each of their nodes
contains a single digit. Add the two numbers and return the sum as a linked
list.

You may assume the two numbers do not contain any leading zero,  except the
number 0 itself.

Ex 1
2 .. 4 .. 3
5 .. 6 .. 4
7 .. 0 .. 8

Input: l1 = [2, 4, 3],  l2 = [5, 6, 4]
Output: [7, 0, 8]
Explanation: 342 + 465 = 807.

Input: l1 = [0],  l2 = [0]
Output: [0]

Input: l1 = [9, 9, 9, 9, 9, 9, 9],  l2 = [9, 9, 9, 9]
Output: [8, 9, 9, 9, 0, 0, 0, 1]

  9999999
     9999
 ========
 10009998

The number of nodes in each linked list is in the range [1,  100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading
zeros.

"""


class ListNode:
    def __init__(self,  val=0,  next=None):
        self.val = val
        self.next = next

    def add_next_digit(self,  digit):
        nextNode = ListNode(digit)
        self.next = nextNode
        return nextNode


class ListNodeGenerator:
    def buildListNode(self,  digits):
        # non empty array of digits- given
        rootNode = None
        node = None
        for d in digits:
            if node:
                node = node.add_next_digit(d)
            else:
                node = ListNode(d)
                rootNode = node
        return rootNode

    def convertToList(self,  ln: ListNode) -> []:
        result = []
        while ln is not None:
            result.append(ln.val)
            ln = ln.next
        return result


class Solution:
    def addTwoNumbers(self,  l1: ListNode,  l2: ListNode) -> ListNode:
        root_result = ListNode(0)
        result = root_result
        carry = 0
        while l1 is not None or l2 is not None or carry > 0:
            left_val = 0
            right_val = 0
            if l1 is not None:
                left_val = l1.val
            if l2 is not None:
                right_val = l2.val
            tmp = left_val + right_val + carry

            # 8+8=16,  keep 6 in tmp,  1 in carry
            carry = 0
            if tmp >= 10:
                tmp -= 10
                carry = 1

            # add new node
            result.next = ListNode(tmp)
            result = result.next

            # move to next digit
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
                l2 = l2.next

        return root_result.next


def test_ListNodeGenerator_GenerateExpectedNodeList():
    numbers_list = [3,  4,  3,  5,  4]
    g = ListNodeGenerator()
    root_node = g.buildListNode(numbers_list)
    node = root_node
    for i in numbers_list:
        n = node.val
        assert i == n
        node = node.next
    returned_list = g.convertToList(root_node)
    assert returned_list == numbers_list


def test_Solution_AddTwoNumbers():
    g = ListNodeGenerator()
    nlOne = g.buildListNode([2, 4, 3])
    nlTwo = g.buildListNode([5, 6, 4])
    s = Solution()
    result = s.addTwoNumbers(nlOne,  nlTwo)
    assert [7, 0, 8] == g.convertToList(result)


def test_Solution_AddOneNull():
    g = ListNodeGenerator()
    nlOne = g.buildListNode([])
    nlTwo = g.buildListNode([0, 1])
    s = Solution()
    result = s.addTwoNumbers(nlOne,  nlTwo)
    assert [0, 1] == g.convertToList(result)


#  10
# 210
# 220

def test_Solution_AddTwoNumbersUnevenSizes():
    g = ListNodeGenerator()
    nlOne = g.buildListNode([0, 1])
    nlTwo = g.buildListNode([0, 1, 2])
    s = Solution()
    result = s.addTwoNumbers(nlOne,  nlTwo)
    assert [0, 2, 2] == g.convertToList(result)


def test_Solution_AddTwoZeros():
    g = ListNodeGenerator()
    nlOne = g.buildListNode([0])
    nlTwo = g.buildListNode([0])
    s = Solution()
    result = s.addTwoNumbers(nlOne,  nlTwo)
    assert [0] == g.convertToList(result)

#  99
#   1
# 100


def test_Solution_AddTwoNumbersWithCarry():
    g = ListNodeGenerator()
    nlOne = g.buildListNode([9, 9])
    nlTwo = g.buildListNode([1])
    s = Solution()
    result = s.addTwoNumbers(nlOne,  nlTwo)
    assert [0, 0, 1] == g.convertToList(result)


def test_Solution_AddTwoLongNumbers():
    g = ListNodeGenerator()
    nlOne = g.buildListNode([9, 9, 9, 9, 9, 9, 9])
    nlTwo = g.buildListNode([9, 9, 9, 9])
    s = Solution()
    result = s.addTwoNumbers(nlOne,  nlTwo)
    assert [8, 9, 9, 9, 0, 0, 0, 1] == g.convertToList(result)
