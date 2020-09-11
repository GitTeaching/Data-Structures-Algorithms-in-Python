DEFAULT_CAPACITY = 10

# Using an Array(py list) Circularly 
class ListQueue:
	def __init__(self):
		self.queue = [None]*DEFAULT_CAPACITY
		self.size = 0
		self.front_ind = 0

    # size is current len (nbr) of elements in queue, without Nones
    # len(self.queue) is length of queue, with Nones
	def __len__(self):
		return self.size 

	def is_empty(self):
		return self.size == 0

	def first(self):
		if self.is_empty():
			raise Empty('Queue is empty')
		return self.queue[self.front_ind]

	def dequeue(self):
		if self.is_empty():
			raise Empty("Queue is empty, can't dequeue")
		deq_element = self.queue[self.front_ind]
		self.queue[self.front_ind] = None
		self.front_ind = (self.front_ind + 1) % len(self.queue)
		self.size -= 1
		return deq_element

	def enqueue(self, data):
		if self.size == len(self.queue):
			self.resize(2 * len(self.queue))
		tail = (self.front + self.size) % len(self.queue)
		self.queue[tail] = data
		self.size += 1

	def resize(self, capacity):
		





# definition for an Empty exception class.
class Empty(Exception):
	"""Error attempting to access an element from an empty container."""
	pass

def main():
	print()

if __name__ == '__main__':
	main()