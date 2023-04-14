
from containers.BinaryTree import BinaryTree, Node


class Heap(BinaryTree):
    '''
    FIXME:
    Heap is currently not a subclass of BinaryTree.
    You should make the necessary changes in the class declaration line above
    and in the constructor below.
    '''

    def __init__(self, xs=None):
        '''
        FIXME:
        If xs is a list (i.e. xs is not None),
        then each element of xs needs to be inserted into the Heap.
        '''
        super().__init__()
        self.num_nodes = 0
        if xs:
            for x in xs:
                self.insert(x)

    def __repr__(self):
        '''
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        '''
        if self.root:
            return Heap._is_heap_satisfied(self.root)
        return True

    @staticmethod
    def _is_heap_satisfied(node):
        '''
        FIXME:
        Implement this method.
        '''
        ret = True
        if node.left:
            ret &= node.value <= node.left.value
            ret &= Heap._is_heap_satisfied(node.left)
        if node.right:
            ret &= node.value <= node.right.value
            ret &= Heap._is_heap_satisfied(node.right)
        return ret

    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        self.num_nodes += 1
        binary_str = bin(self.num_nodes)[3:]
        if self.root is None:
            self.root = Node(value)
        else:
            Heap._insert(self.root, value, binary_str)

    @staticmethod
    def _insert(node, value, binary_str):
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                node.left = Node(value)
            else:
                Heap._insert(node.left, value, binary_str[1:])
            if node.value > node.left.value:
                node.value, node.left.value = node.left.value, node.value
        if binary_str[0] == '1':
            if len(binary_str) == 1:
                node.right = Node(value)
            else:
                Heap._insert(node.right, value, binary_str[1:])
            if node.value > node.right.value:
                node.value, node.right.value = node.right.value, node.value

    def insert_list(self, xs):
        '''
        Given a list xs, insert each element of xs into self.

        FIXME:
        Implement this function.
        '''
        for x in xs:
            self.insert(x)

    def find_smallest(self):
        '''
        Returns the smallest value in the tree.

        FIXME:
        Implement this function.
        '''
        if not self.root:
            return None
        return self._find_smallest(self.root)

    def _find_smallest(self, node):
        if not node:
            return self.root.value
        left_value = self._find_smallest(node.left)
        right_value = self._find_smallest(node.right)
        if node.value < left_value and node.value < right_value:
            return node.value
        elif left_value < node.value and left_value < right_value:
            return left_value
        else:
            return right_value

    def remove_min(self):
        '''
        Removes and returns the minimum element from the heap.
        '''
        binary_str = bin(self.num_nodes)[3:]
        if self.root is None:
            return None
        elif not binary_str:
            min_value = self.root.value
            self.root = None
            self.num_nodes = 0
            return min_value
        else:
            Heap._remove_bottom_right(self.root, binary_str)
            self.num_nodes -= 1
            self.root.value = Heap.replace_value
            Heap._trickle_down(self.root)
            return self.root.value

    @staticmethod
    def _remove_bottom_right(node, binary_str):
        if node is None:
            return node
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                if node.right:
                    Heap.replace_value = node.right.value
                    node.right = None
                elif node.left:
                    Heap.replace_value = node.left.value
                    node.left = None
                else:
                    return None
            else:
                Heap._remove_bottom_right(node.left, binary_str[1:])
        if binary_str[0] == '1':
            if len(binary_str) == 1:
                if node.right:
                    Heap.replace_value = node.right.value
                    node.right = None
                elif node.left:
                    Heap.replace_value = node.left.value
                    node.left = None
                else:
                    return None
            else:
                Heap._remove_bottom_right(node.right, binary_str[1:])

    @staticmethod
    def _trickle_down(node):
        while node.left:
            min_child = node.left
            if node.right and node.right.value < min_child.value:
                min_child = node.right
            if node.value > min_child.value:
                node.value, min_child.value = min_child.value, node.value
                node = min_child
            else:
                break
