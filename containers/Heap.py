'''
This file implements the Heap data structure as a subclass of the BinaryTree.
The book implements Heaps using an *implicit* tree with an *explicit* vector implementation,
so the code in the book is likely to be less helpful than the code for the other data structures.
The book's implementation is the traditional implementation because it has a faster constant factor
(but the same asymptotics).
This homework is using an explicit tree implementation to help you get more practice with OOP-style programming and classes.
'''

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
        
        #self.root = None
        

    def __repr__(self):
        '''
        Notice that in the BinaryTree class,
        we defined a __str__ function,
        but not a __repr__ function.
        Recall that the __repr__ function should return a string that can be used to recreate a valid instance of the class.
        Thus, if you create a variable using the command Heap([1,2,3])
        it's __repr__ will return "Heap([1,2,3])"

        For the Heap, type(self).__name__ will be the string "Heap",
        but for the AVLTree, this expression will be "AVLTree".
        Using this expression ensures that all subclasses of Heap will have a correct implementation of __repr__,
        and that they won't have to reimplement it.
        '''
        return type(self).__name__ + '(' + str(self.to_list('inorder')) + ')'

    def is_heap_satisfied(self):
        '''
        Whenever you implement a data structure,
        the first thing to do is to implement a function that checks whether
        the structure obeys all of its laws.
        This makes it possible to automatically test whether insert/delete functions
        are actually working.
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

        FIXME:
        Implement this function.

        HINT:
        The pseudo code is
        1. Find the next position in the tree using the binary representation of the total number of nodes
            1. You will have to explicitly store the size of your heap in a variable (rather than compute it) to maintain the O(log n) runtime
            1. See https://stackoverflow.com/questions/18241192/implement-heap-using-a-binary-tree for hints
        1. Add `value` into the next position
        1. Recursively swap value with its parent until the heap property is satisfied

        HINT:
        Create a @staticmethod helper function,
        following the same pattern used in the BST and AVLTree insert functions.
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
    
    def _find_smallest(self,node):
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
            print("we are here")
            min_value = self.root.value
            self.root = None
            self.num_nodes = 0
            return min_value
        else: 
            Heap._remove_bottom_right(self.root, binary_str)
            print("Heap.replace_value=", Heap.replace_value)
            self.num_nodes -= 1
            left_child = self.root.left
            print("left_child before change=", left_child)
            left_child = self.root.left
            print("left_child=", left_child)
            print()
            print(str(self))
            self.root.value = Heap.replace_value
            print("self.root.value=", self.root.value)
            print("self.root=", self.root)
            print() 
            print() 
            Heap._trickle_down(self.root)
            return self.root.value

    @staticmethod
    def _remove_bottom_right(node, binary_str):
        if node is None:
            return node
        print("binary_str=", binary_str)
        if binary_str[0] == '0':
            if len(binary_str) == 1:
                if node.right:
                    Heap.replace_value = node.right.value
                    node.right = None
                    #return replace_value
                elif node.left:
                    Heap.replace_value = node.left.value
                    node.left = None
                    #return replace_value
                else:
                    return None
            else:
                Heap._remove_bottom_right(node.left, binary_str[1:])
                #if replace_value is not None:
                    #return replace_value
        if binary_str[0] == '1':
            if len(binary_str) == 1:
                if node.right:
                    Heap.replace_value = node.right.value
                    node.right = None
                    #print("# replace_value=", replace_value)
                elif node.left:
                    print("are we here")
                    Heap.replace_value = node.left.value
                    node.left = None
                    #return replace_value
                else:
                    return None
            else:
                print("we are at the very end")
                Heap._remove_bottom_right(node.right, binary_str[1:])
        
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

