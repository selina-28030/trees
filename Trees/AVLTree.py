'''
This file implements the AVL Tree data structure.
The functions in this file are considerably harder than the functions in the BinaryTree and BST files.
'''

from Trees.BinaryTree import BinaryTree, Node
from Trees.BST import BST

class AVLTree(BST):
	def __init__(self, xs=None):
		
		super().__init__()
        	if xs:
            		self.insert_list(xs)

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
        Returns True if the avl tree satisfies that all nodes have a balance factor in [-1,0,1].
        '''
        	return AVLTree._is_avl_satisfied(self.root)

	@staticmethod
    	def _is_avl_satisfied(node):
        '''
        FIXME:
        Implement this function.
        '''
		if node is None:
			return True
		return AVLTree._balance_factor(node) in [-1, 0, 1] and AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)

    @staticmethod
    def _left_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''
	

    @staticmethod
    def _right_rotate(node):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of tree rotations,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.
        '''


    def insert(self, value):
        '''
        FIXME:
        Implement this function.

        The lecture videos provide a high-level overview of how to insert into an AVL tree,
        and the textbook provides full python code.
        The textbook's class hierarchy for their AVL tree code is fairly different from our class hierarchy,
        however, so you will have to adapt their code.

        HINT:
        It is okay to add @staticmethod helper functions for this code.
        The code should look very similar to the code for your insert function for the BST,
        but it will also call the left and right rebalancing functions.
        '''
