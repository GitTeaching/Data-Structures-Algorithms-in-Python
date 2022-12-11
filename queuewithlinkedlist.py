class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def peek(self):
        if self.first:
            return self.first.data
        return None

    def enqueue(self, data):
        node = Node(data)
        if self.length == 0:
            self.first = node
            self.last = node
        else:
            self.last.next = node
            self.last = node
        self.length +=1

    def dequeue(self):
        if self.length == 0:
            return None       
        dequeueed = self.first.data
        if self.length == 1:
            self.last = None
        self.first = self.first.next
        self.length -=1
        return dequeueed


myqueue = Queue()

myqueue.enqueue('google.com')
myqueue.enqueue('udemy.com')

print(myqueue.peek())

myqueue.enqueue('youtube.com')
print(myqueue.peek())

print(myqueue.dequeue())
print(myqueue.dequeue())
print(myqueue.dequeue())

print(myqueue.peek(), myqueue.length)

myqueue.enqueue('apple.com')
print(myqueue.peek())