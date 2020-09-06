class Node:
	def __init__(self, data):
		self.data = data
		self.prev = None
		self.next = None


class DoublyLinkedList:
	def __init__(self):
		self.head = None

	# traverse and print list
	def linkedlistprint(self):
		node = self.head
		while node is not None:
			print(node.data)
			node = node.next

	#insert node at the begining : push
	def push(self, newdata):
		newNode = Node(newdata)
		newNode.next = self.head
		if self.head is not None:
			self.head.prev = newNode
		self.head = newNode

	#insert node at th end : append
	def append(self, newdata):
		newNode = Node(newdata)
		node = self.head
		if node is None:
			self.head = newNode
			return
		while node.next is not None:
			node = node.next
		node.next = newNode
		newNode.prev = node

	def search(self, data):
		current = self.head
		while current is not None:
			if current.data == data:
				return True
			current = current.next
		return False

	def length(self):
		lLen = 0
		current = self.head
		while current is not None:
			lLen += 1
			current = current.next
		return lLen

	def lengthRecursive(self, node):
		if node is None:
			return 0
		else:
			return 1 + self.lengthRecursive(node.next)


def main():
	dlkl = DoublyLinkedList()
	dlkl.head = Node(2)
	# add new node with data=0 1 at the begining
	dlkl.push(1)
	dlkl.push(0)
	# append new node with data=3
	dlkl.append(3)
	# traverse and print list
	dlkl.linkedlistprint()
	# search element
	print(dlkl.search(3))
	print(dlkl.search(6))
	# length od a list - iterative
	print("Length = %i" %(dlkl.length()))
	# length od a list - recursive 
	print("Length = %i" %(dlkl.lengthRecursive(dlkl.head)))

if __name__ == "__main__":
	main()