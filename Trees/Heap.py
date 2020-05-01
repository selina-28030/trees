'''
'''
from Trees.BinaryTree import BinaryTree, Node

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
        if xs: 
            self.insert_list(xs)


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
        return type(self).__name__+'('+str(self.to_list('inorder'))+')'


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
        The lecture videos have the exact code you need,
        except that their method is an instance method when it should have been a static method.
        '''
        left = True
        right = True
        if node.left:
            if node.value <= node.left.value:
                left = Heap._is_heap_satisfied(node.left)
            else:
                return False
        if node.right:
            if node.value <= node.right.value:
                right = Heap._is_heap_satisfied(node.right)
            else:
                return False
        return right and left
     
    @staticmethod
    def size(node):

        if node is None:
            return 0
        stack=[]
        stack.append(node)
        size=1
        while stack:
            node=stack.pop()
            if node.left:
                size+=1
                stack.append(node.left)
            if node.right:
                size+=1
                stack.append(node.right)
        return size

        
    def insert(self, value):
        '''
        Inserts value into the heap.
        '''
        if self.root is None:
            self.root = Node(value)
            self.root.descendents = 1
        else:
            tree_size = size(node.root)
            tree_size = tree_size + 1
            tree_size = bin(tree_size).replace("0b", "")
            tree_size = tree_size[1:]
            cur_node = node.root
            for num in tree_size:
                if num == '0':
                    cur_node = node.left
                if num == '1':
                    cur_node = node.right
            cur_node = Node(value)

    @staticmethod
    def _trickle_up(node, value):   
        if Heap._is_heap_satisfied(node) == True: 
            return node
        if node.left and node.left.value > node.value:
            node.left = Heap._trickle_up(node.left, value)
        if node.right and node.right.value > node.value:
            node.right = Heap._trickle_up(node.right, value)
        if node.left:
            if node.left.value == value: 
                new_parent = node.left.value
                new_leftchild = node.value
                
                node.value = new_parent
                node.left.value = new_leftchild
        
        if node.right:
            if node.right.value == value: 
                new_parent = node.right.value
                new_rightchild = node.value

                node.value = new_parent
                node.right.value = new_rightchild

        return node
            


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
        This function is not implemented in the lecture notes,
        but if you understand the structure of a Heap it should be easy to implement.

        HINT:
        Create a recursive staticmethod helper function,
        similar to how the insert and find functions have recursive helpers.
        '''
        node = self.root
        return Heap._find_smallest(node).value
        
    
    @staticmethod
    def _find_smallest(node):
        return node.value


    def remove_min(self):
        '''
        Removes the minimum value from the Heap. 
        If the heap is empty, it does nothing.

        FIXME:
        Implement this function.
        '''
