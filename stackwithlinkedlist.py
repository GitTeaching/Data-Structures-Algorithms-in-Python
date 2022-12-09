class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def peek(self):
        if self.top:
            return self.top.data
        return None

    def push(self, data):
        node = Node(data)
        if self.length == 0:
            self.bottom = node
        node.next = self.top
        self.top = node
        self.length +=1

    def pop(self):
        if self.length == 0:
            return None
        poped = self.top.data
        if self.length == 1:
            self.bottom = None
        self.top = self.top.next
        self.length -=1
        return poped


mystack = Stack()

mystack.push('google.com')
mystack.push('udemy.com')

print(mystack.peek())

mystack.push('youtube.com')
print(mystack.peek())

print(mystack.pop())
print(mystack.pop())
print(mystack.pop())

print(mystack.peek(), mystack.length)

mystack.push('apple.com')
print(mystack.peek())