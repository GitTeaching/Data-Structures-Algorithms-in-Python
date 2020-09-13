## Binary Tree implementation 

class Node:
	def __init__(self, data):
		self.data = data
		self.left = None
		self.right = None

class BinaryTree:
	def __init__(self):
		self.root = None

	def get_root(self):
		return self.root

	# Binary Tree - Inorder traversal insert - Recursive
	def add(self, data):
		if self.root is None:
			self.root = Node(data)
		else:
			self._add(self.root, data)
	def _add(self, node, data):
		if data < node.data:
			if node.left is not None:
				self._add(node.left, data)
			else:
				node.left = Node(data)
		else:
			if node.right is not None :
				self._add(node.right, data)
			else:
				node.right = Node(data)

    # Binary Tree - In-order traversal - Recursive
	def print_tree_inorder(self):
		if self.root:
			self._print_tree_inorder(self.root)
		else:
			print("Tree is Empty")
	def _print_tree_inorder(self, node):
		if node:
			self._print_tree_inorder(node.left)
			print(str(node.data))
			self._print_tree_inorder(node.right)

	# Binary Tree - In-order traversal - using Stack
	def print_tree_inorder_stack(self, root):
		if root is None:
			return 
		stack = []
		current = root
		while current or stack is not None:
			if current:
				stack.append(current)
				current = current.left
			else:
				current = stack.pop()
				print(current.data)
				current = current.right

    # Binary Tree - Pre-order traversal - Recursive
	def print_tree_preorder(self, node):
		if node:
			print(node.data)
			self.print_tree_preorder(node.left)
			self.print_tree_preorder(node.right)

    # Binary Tree - Post-order traversal - Recursive
	def print_tree_postorder(self, node):
		if node:
			self.print_tree_postorder(node.left)
			self.print_tree_postorder(node.right)
			print(node.data)

	# Binary Tree - Level order traversal (BFS) using Queue
	def print_tree_levelorder(self, root):
		if root is None:
			return
		queue = []
		queue.append(root)
		while (len(queue) > 0):
			print(queue[0].data)
			node = queue.pop(0)
			if node.left is not None:
				queue.append(node.left)
			if node.right is not None:
				queue.append(node.right)

	# Binary Tree - Level order traversal (BFS) using Queue
	def print_level_by_level(self, root):
		if root is None:
			return
		queue = []
		queue.append(root)
		while queue:
			count = len(queue)
			while count > 0:
				node = queue.pop(0)
				print(node.data, end=' ')
				if node.left is not None:
					queue.append(node.left)
				if node.right is not None:
					queue.append(node.right)
				count -= 1
			print('')

	# Binary Search Tree - Inorder traversal  - Recursive
	def search(self, val):
		if self.root is not None:
			return self._search(self.root, val)
		return False
	def _search(self, node, val):
		if node.data == val:
			return True
		elif val < node.data and node.left is not None:
			return self._search(node.left, val)
		elif val > node.data and node.right is not None:
			return self._search(node.right, val)
		return False

	def delete_tree(self):
		self.root = None

	def max_height_tree(self, root):
		if root is None:
			return 0
		leftHeight = self.max_height_tree(root.left)
		rightHeight = self.max_height_tree(root.right)
		if leftHeight > rightHeight:
			return leftHeight + 1
		else:
			return rightHeight + 1

	def maxDepth(self, root) -> int:
		if root is not None:
			return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
		else:
			return 0

	def is_height_balanced(self, root):
		if root is None:
			return True
		left = self.maxDepth(root.left)
		right = self.maxDepth(root.right)
		return abs(left - right) <= 1 and self.is_height_balanced(root.left) and self.is_height_balanced(root.right)

	def print_path_between_nodes(self, root, n1, n2):
		path1 = []
		path2 = []
		self.get_path(root, path1, n1)
		self.get_path(root, path2, n2)
		#get intersection point
		i = 0
		j = 0
		intersect = -1
		while i != len(path1) or j != len(path2):
			if i==j and path1[i]==path2[j]:
				i += 1
				j += 1
			else:
				intersect = j - 1
				break
		for i in range(len(path1)-1, intersect-1, -1):
			print(path1[i], end=" ")
		for j in range(intersect+1, len(path2)):
			print(path2[j], end=" ")

	def get_path(self, root, path, node):
		if root is None:
			return False
		path.append(root.data)
		if root.data == node:
			return True
		if self.get_path(root.left, path, node) or self.get_path(root.right, path, node):
			return True
		path.pop()
		return False

def main():
	mytree = BinaryTree()
	mytree.add(8)
	mytree.add(6)
	mytree.add(10)
	mytree.add(12)
	mytree.add(14)
	mytree.add(5)
	mytree.add(2)
	mytree.add(7)
	mytree.add(9)
	#mytree.print_tree_inorder()
	#mytree.print_tree_inorder_stack(mytree.root)
	#mytree.print_tree_preorder(mytree.root)
	#mytree.print_tree_postorder(mytree.root)
	#mytree.print_tree_levelorder(mytree.root)
	mytree.print_level_by_level(mytree.root)
	# print(mytree.get_root().data)
	print(mytree.search(8))
	print("The max depth is:", mytree.max_height_tree(mytree.root))
	print("The max depth is:", mytree.maxDepth(mytree.root))
	print(mytree.is_height_balanced(mytree.root))
	mytree.print_path_between_nodes(mytree.root, 2, 10)


if __name__ == "__main__":
	main()