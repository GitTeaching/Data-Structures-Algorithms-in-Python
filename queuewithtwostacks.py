class MyQueue:

    def __init__(self):
        self.first = []
        self.last = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        while self.first:
            self.last.append(self.first.pop())
        self.first.append(x)
        while self.last:
            self.first.append(self.last.pop())

    def pop(self):
        """
        :rtype: int
        """
        return self.first.pop()
        
    def peek(self):
        """
        :rtype: int
        """
        return self.first[-1]
        
    def empty(self):
        """
        :rtype: bool
        """
        return not self.first
        

obj = MyQueue()
obj.push("google.com")
obj.push("youtube.com")
print(obj.pop())
print(obj.peek())
print(obj.empty())