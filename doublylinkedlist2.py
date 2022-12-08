
class DoublyLinkedList:
    def __init__(self, value):
        self.head = {
            'value' : value,
            'next': None,
            'prev': None
        }
        self.tail = self.head
        self.length = 1    


    def __str__(self):
        return str(self.__dict__)


    def print_list(self):
        my_list = []
        currNode = self.head
        while currNode:
            my_list.append(currNode['value'])
            currNode = currNode['next']
        return my_list


    def append(self, value):
        node = {
            'value': value,
            'next': None,
            'prev': None
        }
        node['prev'] = self.tail
        self.tail['next'] = node
        self.tail = node
        self.length += 1
    

    def preppend(self, value):
        node = {
            'value': value,
            'next': None,
            'prev': None
        }
        node['next'] = self.head
        self.head['prev'] = node
        self.head = node
        self.length += 1
    
    def traverse_to_index(self, index):
        currNode = self.head
        i = 0
        while i != index:
            currNode = currNode['next']
            i += 1
        return currNode

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)         
        if index <= 0:
            return self.preppend(value)      
        newNode = {
            'value': value,
            'next': None,
            'prev': None
        }
        currNode = self.traverse_to_index(index-1)
        follower = currNode['next']
        currNode['next'] = newNode
        newNode['prev'] = currNode
        newNode['next'] = follower
        follower['prev'] = newNode
        self.length += 1
    
    def remove(self, index):
        if index >= self.length:
            return False
        if index == 0 and self.head:
            self.head = self.head['next']
            self.length -= 1
            return
        if index == self.length-1:
            currNode = self.traverse_to_index(index-1)
            currNode['next'] = None
            self.tail = currNode
            self.length -= 1
            return
        currNode = self.traverse_to_index(index-1)
        unwatedNode = currNode['next']        
        currNode['next'] = unwatedNode['next']
        self.length -= 1


my_linked_list = DoublyLinkedList(10)

my_linked_list.append(5)

my_linked_list.preppend(7)

my_linked_list.insert(1, 63)
my_linked_list.insert(0, 456)

#my_linked_list.remove(4)

print(my_linked_list)
print(my_linked_list.print_list())