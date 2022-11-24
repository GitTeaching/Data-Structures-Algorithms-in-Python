
class LinkedList:
    def __init__(self, value):
        self.head = {
            'value' : value,
            'next': None
        }
        self.tail = self.head
        self.length = 1    

    def __str__(self):
        return str(self.__dict__)

    def append(self, value):
        node = {
            'value': value,
            'next': None
        }
        self.tail['next'] = node
        self.tail = node
        self.length += 1
    
    def preppend(self, value):
        node = {
            'value': value,
            'next': None
        }
        node['next'] = self.head
        self.head = node
        self.length += 1


my_linked_list = LinkedList(10)
my_linked_list.append(5)
print(my_linked_list)
my_linked_list.preppend(7)
my_linked_list.append(99)
my_linked_list.preppend(341)
print(my_linked_list)