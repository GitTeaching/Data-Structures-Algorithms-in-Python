"""
Traversing a tree means visiting every node in the tree. You might, for instance, want to add all the values in the tree or find the largest one. 
For all these operations, you will need to visit each node of the tree.

Linear data structures like arrays, stacks, queues, and linked list have only one way to read the data. 
But a hierarchical data structure like a tree can be traversed in three different ways: inorder, preorder and postorder.

inoreder : Left subtree -> root -> right subtree
preorder : root -> Left subtree -> right subtree
postorder : Left subtree ->  right subtree -> root

"""

# A node class with data value and two pointers to its left and right children
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# Inorder tree traversal
def inorder(root):
	if root:
		inorder(root.left)
		print(str(root.data))
		inorder(root.right)

# preorder tree traversal
def preorder(root):
	if root:
		print(str(root.data))
		preorder(root.left)
		preorder(root.right)


# postorder tree traversal
def postorder(root):
	if root:
		postorder(root.left)
		postorder(root.right)
		print(str(root.data))


def main():
	root = Node(1)
	root.left = Node(12)
	root.right= Node(9)
	root.left.left = Node(5)
	root.left.right = Node(6)


	print("Inorder traversal ")
	if root:
		inorder(root)
	else:
		print("Tree is Empty")


	print("Preorder traversal ")
	if root:
		preorder(root)
	else:
		print("Tree is Empty")


	print("Postorder traversal ")
	if root:
		postorder(root)
	else:
		print("Tree is Empty")


if __name__ == '__main__':
	main()
