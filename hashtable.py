
class HashTable:
    def __init__(self, size):
        self.size = size
        self.data = [[] for _ in range(self.size)]

    def __str__(self):
        return str(self.data)

    def hash(self, key):
        return len(key) % self.size


    def set(self, key, value):
        hashed_key = self.hash(key)
        self.data[hashed_key].append([key, value])


    def get(self, key):
        hashed_key = self.hash((key))
        reference = self.data[hashed_key]
        if reference:
            for i in range(len(reference)):
                if reference[i][0] == key:
                    return reference[i][1]
        return -1

    
    def keys(self):
        if not self.data:
            return None

        all_keys = []
        for element in self.data:
            if element:
                # Check for collisions 
                if len(element) > 1:                
                    for k in element:
                        all_keys.append(k[0])
                else:
                    all_keys.append(element[0][0])  
        
        return all_keys


my_ht = HashTable(10)

my_ht.set('grappes', 1000)
my_ht.set('grappess', 54)
my_ht.set('grappesss', 93)
my_ht.set('grapsss', 5)

print(my_ht)

print(my_ht.get('grapsss'))
print(my_ht.get('grappes'))
print(my_ht.get('test'))

print(my_ht.keys())
