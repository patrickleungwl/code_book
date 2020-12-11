import unittest
import tree_py


class test_bst(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_threeinputs_expect_same_result(self):
        b = tree_py.bst()
        numbers_list = [3, 4, 3, 5, 4]
        self.assertEqual(b.build(numbers_list), '3 4 3 5 4')

        numbers_list = [3, 4, 5, 4, 3]
        self.assertEqual(b.build(numbers_list), '3 4 3 5 4')

        numbers_list = [3, 4, 5, 3, 4]
        self.assertEqual(b.build(numbers_list), '3 4 3 5 4')


    def test_num_ways_same_result(self):
        numbers_list = [3, 4, 3, 5, 4]
        self.assertEqual(tree_py.num_ways(number_list), 5)


unittest.main()

