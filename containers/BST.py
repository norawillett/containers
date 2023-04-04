'''
This file implements the Binary Search Tree data structure.
'''

from containers.BinaryTree import BinaryTree, Node


class BST(BinaryTree):
    '''
    The BST is a superclass of BinaryTree.
    and we don't have to reimplement them.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the BST.
        '''
        super().__init__()
        if xs:
            self.insert_list(xs)

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def __iter__(self):
        self.index = 0
        self.list = self.to_list('inorder')
        return self

    def __next__(self):
        if self.index < super().__len__():
            value = self.list[self.index]
            self.index += 1
            return value
        else:
            raise StopIteration()

    def __eq__(self, t2):
        '''
        This method checks to see if the contents of self and t2 are equal.
        The expression `a == b` desugars to `a.__eq__(b)`.

        NOTE:
        We only care about "semantic" equality,
        and not "syntactic" equality.
        That is, we do not care about the tree structure itself,
        and only care about the contents of what the tree contains.

        HINT:
        Convert the contents of both trees into a sorted list,
        then compare those sorted lists for equality.
        '''
        self_list = self.to_list('inorder')
        t2_list = t2.to_list('inorder')
        return sorted(t2_list) == sorted(self_list)

    def is_bst_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        are actually working.
        '''
        if self.root:
            return BST._is_bst_satisfied(self.root)
        return True

    @staticmethod
    def _is_bst_satisfied(node):
        '''
        FIXME:
        The current implementation has a bug:

        HINT:
        '''
        ret = True
        if node.left:
            if node.value >= BST._find_largest(node.left):
                ret &= BST._is_bst_satisfied(node.left)
            else:
                ret = False
        if node.right:
            if node.value <= BST._find_smallest(node.right):
                ret &= BST._is_bst_satisfied(node.right)
            else:
                ret = False
        return ret

    def insert(self, value):
        if self.root:
            BST._insert(self.root, value)
        else:
            self.root = Node(value)

    @staticmethod
    def _insert(node, value):
        if value <= node.value:
            if node.left:
                BST._insert(node.left, value)
            else:
                node.left = Node(value)
        if value >= node.value:
            if node.right:
                BST._insert(node.right, value)
            else:
                node.right = Node(value)

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.

        HINT:
        Repeatedly call the insert method.
        '''
        for x in xs:
            if self.root:
                self._insert(self.root, x)
            else:
                self.root = Node(x)

    def __contains__(self, value):
        '''
        Recall that `x in tree` desugars to `tree.__contains__(x)`.
        '''
        return self.find(value)

    def find(self, value):
        '''
        Returns whether value is contained in the BST.

        FIXME:
        Implement this function.
        '''
        if not self.root:
            return None
        else:
            return BST._find(value, self.root)

    @staticmethod
    def _find(value, node):
        '''
        FIXME:
        Implement this function.
        '''
        if node.value == value:
            return True
        if node.value < value:
            if node.right:
                return BST._find(value, node.right)
            else:
                return False
        if node.value > value:
            if node.left:
                return BST._find(value, node.left)
            else:
                return False

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.
        '''
        if self.root:
            return BST._find_smallest(self.root)
        else:
            raise ValueError('Nothing in tree')

    @staticmethod
    def _find_smallest(node):
        '''
        '''
        assert node is not None
        if not node.left:
            return node.value
        else:
            return BST._find_smallest(node.left)

    def find_largest(self):
        '''
        Returns the largest value in the tree.

        FIXME:
        Implement this function.

        HINT:
        Follow the pattern of the _find_smallest function.
        '''
        if self.root:
            return BST._find_largest(self.root)
        else:
            raise ValueError('Nothing in tree')

    @staticmethod
    def _find_largest(node):
        assert node is not None
        if not node.right:
            return node.value
        else:
            return BST._find_largest(node.right)

    def remove(self, value):
        '''
        Removes value from the BST.
        If value is not in the BST, it does nothing.

        FIXME:
        Implement this function.

        HINT:

        HINT:
        '''
        self.root = BST._remove(value, self.root)

    def remove_list(self, xs):
        for x in xs:
            self.remove(x)

    @staticmethod
    def _remove(value, node):
        if node is None:
            return node
        if node.value > value:
            node.left = BST._remove(value, node.left)
            return node
        if node.value < value:
            node.right = BST._remove(value, node.right)
            return node
        if node.value == value:
            if not node.right and not node.left:
                return None
            if node.right is None:
                return node.left
            elif node.left is None:
                return node.right
            else:
                newnode = BST._find_smallest(node.right)
                node.value = newnode
                node.right = BST._remove(newnode, node.right)
                return node
