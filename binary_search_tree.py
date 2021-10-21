
class BinarySearchTree():
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, value):
        #No Children
        if self.value is None:
            self.value=value
        #Traverse Left
        elif value < self.value:
            if self.left is None:
                self.left = BinarySearchTree(value)
            else:
                self.left.insert(value)
        #Traverse Right
        else: 
            if self.right is None:
                self.right = BinarySearchTree(value)
            else:
                self.right.insert(value)
    
    @staticmethod
    def bulk_insert(list):
        node = BinarySearchTree()
        for i in list:
            node.insert(i)
        return node


    @staticmethod
    def delete(node, value):
        #Found the delete node
        if node.value == value:
            #No children, remove
            if node.left is None and node.right is None:
                node = None
                return
            #Only one Child
            elif node.left is None:
                    node.value = node.right.value
                    node.right = None
            elif node.right is None:
                    node.value = node.left.value
                    node.left = None
            #Two Children, find inorder node and then remove
            else:
                inorder_node = BinarySearchTree.find_minimum(node.right)
                BinarySearchTree.delete(inorder_node, inorder_node.value)
                node.value = inorder_node.value
        #Keep Traversing
        elif value < node.value:
            BinarySearchTree.delete(node.left, value)
        else:
            BinarySearchTree.delete(node.right, value)
        

    @staticmethod
    def search(node, value):
        #Found the Node
        if node.value is None or node.value == value:
            return node
        #Keep Traversing
        if node.left is not None and value < node.value:
            node = node.left
        else:
            node = node.right
        return BinarySearchTree.search(node, value)

    
    @staticmethod
    def sorted_list(node, list=[]):
        if node is not None:
            BinarySearchTree.sorted_list(node.left, list)
            list.append(node.value)
            BinarySearchTree.sorted_list(node.right, list)
        return list
    
    @staticmethod
    def depth(node):
        #Found Bottom
        if node is None:
            return 0
        #Keep Traversing
        min_depth = BinarySearchTree.depth(node.left)
        max_depth = BinarySearchTree.depth(node.right)
        
        return max(min_depth, max_depth) + 1


    @staticmethod
    def find_minimum(node):
        #Traverse Left until there is None
        if node.left is None:
            return node
        else:
            return BinarySearchTree.find_minimum(node.left) 
    
    @staticmethod
    def find(node, level, max_level, res):
        if node is not None:
            level += 1
            #Check left
            BinarySearchTree.find(node.left, level, max_level, res)
            #If we found the max level, assign to res
            if level == max_level:
                res[0] = node.value
                return
            #check right
            BinarySearchTree.find(node.right, level, max_level, res)

    @staticmethod
    def deepest_node(node):
        res = [-1]
        max_level = BinarySearchTree.depth(node)

        BinarySearchTree.find(node, 0, max_level, res)
        return res[0]
    

    def __str__(self):
        left = None if self.left is None else self.left.value
        right = None if self.right is None else self.right.value
        return f'BSTNode {self.value}: Left Node={left}, Right Node={right}'

