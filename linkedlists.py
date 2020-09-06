class Node:
	# constructor
	def __init__(self, data, next=None):
		self.data = data
		self.next = next

class LinkedList:
	def __init__(self):
		self.head = None
    
	def linkedlistprint(self):
		printval = self.head
		while printval is not None:
			print(printval.data)
			printval = printval.next

	def insertAtBegining(self, newdata):
		newNode = Node(newdata)
		newNode.next = self.head
		self.head = newNode

	def insertAtEnd(self, newdata):
		newNode = Node(newdata)
		last = self.head
		if last is None:
			self.head = newNode
			return
		while last.next is not None:
			last = last.next
		last.next = newNode

	def insertAfterNode(self, nodebefore, newdata):
		if nodebefore is None:
			print("The node before is absent")
			return
		newNode = Node(newdata)
		newNode.next = nodebefore.next
		nodebefore.next = newNode

	def insertAfterNodeData(self, databefore, newdata):
		newNode = Node(newdata)
		if self.head == databefore:
			self.head.next = newNode
			return
		else:
			searchedNode = self.head
			while searchedNode.next is not None:
				if searchedNode.data == databefore:
					newNode.next = searchedNode.next
					searchedNode.next = newNode
					return
				searchedNode = searchedNode.next
		print("Node do not exist")

	def removeNodeByData(self, data):
		removedNode = self.head
		if removedNode is not None:
			if removedNode.data == data:
				self.head = removedNode.next
				removedNode = None
				return
			
		while removedNode is not None:
			if removedNode.data == data:
				break
			prev = removedNode
			removedNode = removedNode.next 

		if removedNode == None :
			return

		prev.next = removedNode.next

		removedNode = None

	def reverseLinkedList(self):
		previous = None
		current = self.head
		following = current.next

		while current is not None:
			current.next = previous
			previous = current
			current = following
			if following:
				following = following.next
		self.head = previous

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
	# Creating a linked list with 3 nodes (head and node2 and node3)
	lkl = LinkedList()
	lkl.head = Node(1)
	node2 = Node(2)
	node3 = Node(3)
	lkl.head.next = node2	
	node2.next =  node3

	# inserting a new node at the begining
	lkl.insertAtBegining(newdata=0)

	# inserting a new node at the end
	lkl.insertAtEnd(newdata=6)

	# inserting a new node after node3
	lkl.insertAfterNode(node3, 4)

	# inserting a new node after data=4
	lkl.insertAfterNodeData(4, newdata=5)

	#printing the linkedlist
	lkl.linkedlistprint()

	# inserting a new node at the end and remove it
	lkl.insertAtEnd(newdata=7)
	lkl.linkedlistprint()
	lkl.removeNodeByData(7)
	lkl.linkedlistprint()

	print("Reversed LL: ")
	lkl.reverseLinkedList()
	lkl.linkedlistprint()


if __name__ == "__main__":
	main()