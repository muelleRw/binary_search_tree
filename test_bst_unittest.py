import unittest
from binary_search_tree import BinarySearchTree

class TestBST(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestBST, self).__init__(*args, **kwargs)

        self.bst = BinarySearchTree.bulk_insert([12, 11, 90, 82, 7, 9])

    def test_insert(self):
        node = self.bst
        node.insert(6)
        self.assertEqual(node.left.left.left.value, 6, "Expecting 6")
        

    def test_delete_no_child(self):
        node = self.bst
        BinarySearchTree.delete(node, 9)
        self.assertEqual(node.left.right, None, "Expecting None")
    

    def test_delete_one_child(self):
        node = self.bst
        BinarySearchTree.delete(node, 90)
        self.assertEqual(node.right.value, 82, "Expecting 82")


    def test_delete_two_child(self):
        node = self.bst
        BinarySearchTree.delete(node, 12)
        self.assertEqual(node.value, 82, "Expecting 82")
    

    def test_minimum(self):
        self.assertEqual(self.bst.find_minimum(self.bst).value, 7, "Expecting 7")
    

    def test_sorted(self):
        list = self.bst.sorted_list(self.bst)
        self.assertEqual(list[3], 12, "Expecting 12")


    def test_deepest_node(self):
        node = self.bst
        self.assertEqual(BinarySearchTree.deepest_node(node), 9, "Expecting 9")

        
    def test_depth(self):
        node = self.bst
        self.assertEqual(BinarySearchTree.depth(node), 4, "Expecting 4")



if __name__ == '__main__':
    unittest.main()
