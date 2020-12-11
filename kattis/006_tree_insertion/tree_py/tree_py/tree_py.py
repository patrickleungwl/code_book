
# advanced data structures must be used to store the data 
# and allow to access them very quickly.
#
# A Binary Search Tree (BST) is one example of such a data structure. 
# It holds a collection of values with some comparison operation that
# provides linear ordering on these values.
#
# BST consists of nodes, each of them contains one value and has at most 
# two subnodes: left and right (BST is a binary tree). The left subtree 
# always contains only values strictly less than the node value, the right 
# subtree only values greater than or equal to the node value.
#
# As a consequence, values may easily be looked up by traversing the tree 
# recursively. We begin with the root node and compare its value with the 
# value we are searching for. Depending on the result, we descend either 
# into the left or into the right subtree, but we never need to walk through both.
#
# The figures below show the tree after subsequently adding the following sequence 
# of numbers: 3, 4, 3, 5, 4, 1, and 2.
#
# You may notice that different permutations of the same numbers will often result
#  in the same BST. For example, the tree from the fifth figure above may be 
#  constructed by three different input sequences:
#
# 3, 4, 3, 5, 4
# 3, 4, 5, 4, 3
# 3, 4, 5, 3, 4
# 
# Interesting, isn’t it? Your task is to compute how many different permutations 
# are there that will result into the same BST.
#
# Input
#
# The input will consist of several trees, each of them specified on two lines. 
# The first line contains a single integer N (1≤N≤100), the number of values in 
# the tree. The second line contains N values separated by a space. These values, 
# if inserted in the given order, form a BST to be examined. All values will be 
# between 0 and 1000.
#
# The last tree is followed by a line containing a single zero.
#
# Output
#
# For each tree, output the total number of different permutations that would 
# generate the same Binary Search Tree. As you may notice in the Sample Output, 
# this number may exceed 2^32.
#
#
# Sample Input 1	
# 
# 5
# 3 4 3 5 4
# 7
# 3 4 3 5 4 1 2
# 31
# 16 8 24 4 12 20 28 2 6 10 14 18 22 26 30 1 3 5 7 9 11 13 15 17 19 21 23 25 27 29 31
# 0
# 
# Sample Output 1
# 3
# 45
# 74836825861835980800000
#

from codeprofile import profiler


class node(object):
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

    @profiler.profile_func
    def add_node(self, num):
        if num >= self.num:
            if self.right == None:
                self.right = node(num)
            else:
                self.right.add_node(num)
        else:
            if self.left == None:
                self.left = node(num)
            else:
                self.left.add_node(num)

    @profiler.profile_func
    def get_children(self, children):
        children.append(self.num)
        if self.left != None:
            self.left.get_children(children)
        if self.right != None:
            self.right.get_children(children)


    @profiler.profile_func
    def get_all_children(self):
        result_str = ''
        children = []
        self.get_children(children)
        return str(children)


class bst(object):

    def __init__(self):
        self.matches = {}

    @profiler.profile_func
    def build(self, numbers):
        tree = None
        for n in numbers:
            if tree == None:
                tree = node(n)
            else:
                tree.add_node(n)
        return tree.get_all_children()


    @profiler.profile_func
    def permute(self, numbers, path):
        if len(numbers)==1:            
            path.append(numbers[0])
            if str(path) in self.matches:
                path.pop()
                return

            newtree = self.build(path)
            if self.root_bst == newtree:
                self.matches[str(path)] = 1
            path.pop()
            return

        # B C
        for i in range(0,len(numbers)):
            path.append(numbers[i])
            number = numbers[i]
            numbers.pop(i)  # remove B, only C remain            
            self.permute(numbers, path)
            numbers.insert(i, number)   # put back original number
            path.pop()                  # restore original path


    @profiler.profile_func
    def root_permute(self, numbers):
        self.root_bst = self.build(numbers)
        path = []
        self.permute(numbers, path)
        print(len(self.matches))


nums=[16,8,24,4,12,20,28,2,6]
b = bst()
b.root_permute(nums)


profiler.print_run_stats()

