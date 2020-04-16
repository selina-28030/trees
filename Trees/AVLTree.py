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
        	return AVLTree._balance_factor(self.root)

	@staticmethod
	def _balance_factor(node):
		if node is None:
	    		return 0
		return BinaryTree._height(node.left) - BinaryTree._height(node.right)


	def is_avl_satisfied(self):
        	return AVLTree._is_avl_satisfied(self.root)

	@staticmethod
	def _is_avl_satisfied(node):
		if node is None:
			return True
		return AVLTree._balance_factor(node) in [-1, 0, 1] and AVLTree._is_avl_satisfied(node.left) and AVLTree._is_avl_satisfied(node.right)

   
	#@staticmethod
	#def_left_rotate(node):

	
	#@staticmethod
	#def _right_rotate(node):
		

	#def insert(self, value):

