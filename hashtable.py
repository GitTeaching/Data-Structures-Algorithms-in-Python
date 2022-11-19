
class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(self.size)]


    def hash(self, key):
        return len(key) % self.size


    def set(self, key, value):
        hashed_key = self.hash(key)
        self.data[hashed_key].append([key, value])
        print(self.data)


    def get(self, key):
        hashed_key = self.hash((key))
        reference = self.data[hashed_key]
        if reference:
            for i in range(len(reference)):
                if reference[i][0] == key:
                    return reference[i][1]
        return -1


my_ht = HashTable(10)
my_ht.set('grappes', 1000)
my_ht.set('grappess', 54)
my_ht.set('grappesss', 93)
my_ht.set('grapsss', 5)

print(my_ht.get('grapsss'))
print(my_ht.get('grappes'))
print(my_ht.get('test'))
