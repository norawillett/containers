'''
'''

from containers.BinaryTree import BinaryTree, Node
from containers.BST import BST


class AVLTree(BST):
    '''
    FIXME:
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        Implement this function.
        '''
        super().__init__()

    def balance_factor(self):
        '''
        Returns the balance factor of a tree.
        '''
        return AVLTree._balance_factor(self.root)

    @staticmethod
    def _balance_factor(node):
        '''
        Returns the balance factor of a node.
        '''
        if node is None:
            return 0
        return BinaryTree._height(node.left) - BinaryTree._height(node.right)

    def is_avl_satisfied(self):
        '''
        '''
        return AVLTree._is_avl_satisfied(self.root)

    @staticmethod
    def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
        ret = True
        if not node:
            return True
        if AVLTree._balance_factor(node) not in [-1, 0, 1]:
            return False
        else:
            if node.left:
                ret &= AVLTree._is_avl_satisfied(node.left)
            if node.right:
                ret &= AVLTree._is_avl_satisfied(node.right)
        return ret

    @staticmethod
    def _left_rotate(node):
        '''
        '''

        if node is None or node.right is None:
            return node
        new_node = Node(node.right.value)
        new_node.right = node.right.right
        new_left = Node(node.value)
        new_left.left = node.left
        new_left.right = node.right.left

        new_node.left = new_left
        return new_node

    @staticmethod
    def _right_rotate(node):
        '''
        '''

        if node is None or node.left is None:
            return node
        new_node = Node(node.left.value)
        new_node.left = node.left.left

        new_right = Node(node.value)
        new_right.right = node.right
        new_right.left = node.left.right

        new_node.right = new_right
        return new_node

    def insert(self, value):
        '''
        '''

        if not self.root:
            self.root = Node(value)
        else:
            self.root = AVLTree._insert(self.root, value)

    def insert_list(self, xs):
        for x in xs:
            if self.root:
                self.root = AVLTree._insert(self.root, x)
            else:
                self.root = Node(x)

    @staticmethod
    def _insert(node, value):
        if node is None:
            return Node(value)
        elif value < node.value:
            node.left = AVLTree._insert(node.left, value)
        else:
            node.right = AVLTree._insert(node.right, value)

        if AVLTree._balance_factor(node) > 1:
            if value < node.left.value:
                return AVLTree._right_rotate(node)
            else:
                node.left = AVLTree._left_rotate(node.left)
                return AVLTree._right_rotate(node)
        if AVLTree._balance_factor(node) < -1:
            if value > node.right.value:
                return AVLTree._left_rotate(node)
            else:
                node.right = AVLTree._right_rotate(node.right)
                return AVLTree._left_rotate(node)

        else:
            return node

    @staticmethod
    def _rebalance(node):
        '''
        There are no test cases for the rebalance function,
        so you do not technically have to implement it.
        But both the insert function needs the rebalancing code,
        so I recommend including that code here.
        '''
