class ListStack:
	"""LIFO Stack implementation using a Python list as underlying storage"""
	def __init__(self):
		self.stack = []

	def push(self, data):
		self.stack.append(data)

	def pop(self):
		if self.is_empty():
			raise Empty("Can't pop. Stack is empty")
		return self.stack.pop()

	def is_empty(self):
		if len(self.stack) == 0:
			return True
		return False

	def top(self):
		if self.is_empty():
			raise Empty("Stack is Empty")
		return self.stack[-1]

	def __len__(self):
		return len(self.stack)


# definition for an Empty exception class.
class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass


# reverse file using a stack
def reverse_file(filename):
	stk = ListStack()
	f = open(filename)
	for line in f:
		stk.push(line.rstrip('\n'))
	f.close
	revF = open(filename, 'w')
	while not stk.is_empty():
		revF.write(stk.pop() + '\n')
	revF.close()

# a function for Matching Delimiters {([])}
def is_matched_delim(expr):
	stk = ListStack()
	left = '[{('
	right = ']})'
	for c in expr:
		if c in left:
			stk.push(c)
		elif c in right:
			if stk.is_empty():
				return False
			"""if right.index(c) != left.index(s.pop()):
				return False"""
			if right.index(c) != left.index(stk.top()):
				return False
			if right.index(c) == left.index(stk.top()):
				stk.pop()
	return stk.is_empty()


def main():
	# create a stack - list usage storage
	stack = ListStack()
	stack.push(1)
	stack.push(4)
	stack.push(3)
	print("Length : %i" %(len(stack)))
	stack.pop()
	print("Length : %i" %(len(stack)))
	print(stack.is_empty())
	print("Top of the stack : %i" %(stack.top()))

	# reverse a file line by line
	filename = 'test.txt'
	#reverse_file(filename)
	print("File reversed!")

	print(is_matched_delim('[(5+x)-(y+z)]}'))


if __name__ == '__main__':
	main()