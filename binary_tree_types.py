"""
Binary tree types :

Full Binary tree : is a special type of binary tree in which every parent node/internal node has either two or no children.

Perfect binary tree : is a type of binary tree in which every internal node has exactly two child nodes and all the leaf nodes are at the same level.

Complete binary tree is a binary tree in which all the levels are completely filled except possibly the lowest one, which is filled from the left.
Complete binary tree is a binary tree whose all levels except the last level are completely filled and all the leaves in the last level are all to the left side.

Balanced binary tree, also referred to as a height-balanced binary tree, is defined as a binary tree in which the height of 
the left and right subtree of any node differ by not more than 1.
"""


# A node class with data value and two pointers to its left and right children
class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None


# ----------------------------------------------------------------------------------------------------
# Checking if tree is Full Binary Tree
def is_full_tree(root):
	if root is None:
		return True

	if root.left is None and root.right is None:
		return True

	if root.left is not None and root.right is not None:
		return (is_full_tree(root.left) and is_full_tree(root.right))

	return False

# ----------------------------------------------------------------------------------------------------
# Checking if a tree is Perfect Binary Tree
def get_depth(node):
	depth = 0
	while node is not None:
		depth += 1
		node = node.left
	return depth

def is_perfect_tree(root, depth, level):
	if root is None:
		return True

	if root.left is None and root.right is None:
		return (depth == level+1)

	if root.left is None or root.right is None:
		return False

	return is_perfect_tree(root.left, depth, level+1) and is_perfect_tree(root.right, depth, level+1)

# ----------------------------------------------------------------------------------------------------
# Checking if a tree is Complete Binary Tree
def count_nodes(root):
	count = 0
	if root is None:
		return 0
	return 1 + count_nodes(root.left) + count_nodes(root.right)

def is_complete_tree(root, index, nbr_nodes):
	if root is None:
		return True

	if index >= nbr_nodes:
		return False

	return (is_complete_tree(root.left, 2*index+1, nbr_nodes) and is_complete_tree(root.right, 2*index+2, nbr_nodes))

# ----------------------------------------------------------------------------------------------------
# Checking if a tree is Balanced Binary Tree
class CalculateHeight:
    def __init__(self):
        self.height = 0

def is_balanced_tree(root, height_obj):
    left_height = CalculateHeight()
    right_height = CalculateHeight()

    if root is None:
        return True

    l = is_balanced_tree(root.left, left_height)
    r = is_balanced_tree(root.right, right_height)

    height_obj.height = max(left_height.height, right_height.height) + 1

    if abs(left_height.height - right_height.height) <= 1:
        return l and r

    return False
# ----------------------------------------------------------------------------------------------------
def main():
	root = Node(1)
	root.left = Node(12)
	root.right= Node(9)
	root.left.left = Node(5)
	root.left.right = Node(6)

	if is_full_tree(root):
		print("The tree is a full binary tree")
	else:
		print("The tree is not a full binary full")

	if is_perfect_tree(root, depth=get_depth(root), level=0):
		print("The tree is a perfect binary tree")
	else:
		print("The tree is not a perfect binary full")

	if is_complete_tree(root, index=0, nbr_nodes=count_nodes(root)):
		print("The tree is a complete binary tree")
	else:
		print("The tree is not a complete binary full")

	if is_balanced_tree(root, CalculateHeight()):
		print("The tree is a balanced binary tree")
	else:
		print("The tree is not a balanced binary full")


if __name__ == '__main__':
	main()
