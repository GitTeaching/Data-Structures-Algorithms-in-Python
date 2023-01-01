class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None
    

    def insert(self, value):
        new_node = Node(value)
        if self.root:
            curr_node = self.root
            while curr_node and curr_node.value != value:
                if  value < curr_node.value :
                    if not curr_node.left :
                        curr_node.left = new_node
                        return True
                    else:
                        curr_node = curr_node.left
                else:
                    if not curr_node.right :
                        curr_node.right = new_node
                        return True
                    else:
                        curr_node = curr_node.right
        else:
            self.root = new_node   
            return True 
        
        return False
    
    def lookup(self, value):
        if self.root:
            curr_node = self.root
            while curr_node :
                if curr_node.value == value:
                    return True
                
                if  value < curr_node.value :
                    curr_node = curr_node.left
                else:
                    curr_node = curr_node.right

        return False
    

    def remove(self, value):
        if self.root:     
            curr_node = self.root
            parent_node = None
            while curr_node :
                if  value < curr_node.value :
                    parent_node = curr_node
                    curr_node = curr_node.left 

                elif value > curr_node.value :
                    parent_node = curr_node
                    curr_node = curr_node.right
                
                elif curr_node.value == value:
                    # Option 1: No right child:
                    if curr_node.right == None:
                        if parent_node == None:
                            self.root = curr_node.left
                        else:
                            if curr_node.value < parent_node.value:
                                parent_node.left = curr_node.left
                            elif curr_node.value > parent_node.value:
                                parent_node.right = curr_node.left

                    #Option 2: Right child which doesnt have a left child
                    elif curr_node.right.left == None:
                        curr_node.right.left = curr_node.left
                        if parent_node == None:
                            self.root = curr_node.right
                        else:
                            if curr_node.value < parent_node.value:
                                parent_node.left = curr_node.right
                            elif curr_node.value > parent_node.value:
                                parent_node.right = curr_node.right

                    #Option 3: Right child that has a left child
                    else:
                        #find the Right child's left most child
                        leftmost = curr_node.right.left
                        leftmostParent = curr_node.right
                        while leftmost.left != None:
                            leftmostParent = leftmost
                            leftmost = leftmost.left

                        #Parent's left subtree is now leftmost's right subtree
                        leftmostParent.left = leftmost.right
                        leftmost.left = curr_node.left
                        leftmost.right = curr_node.right

                        if parent_node == None:
                            self.root = leftmost
                        else:
                            if curr_node.value < parent_node.value:
                                parent_node.left = leftmost
                            elif curr_node.value > parent_node.value:
                                parent_node.right = leftmost
                    
                    return True            
                
        return False        



my_bst = BinarySearchTree()
print(my_bst.insert(9))
print(my_bst.insert(4))
print(my_bst.insert(6))
print(my_bst.insert(1))
print(my_bst.insert(20))
print(my_bst.insert(15))
print(my_bst.insert(170))
print(my_bst.insert(3))
print(my_bst.insert(8))

print(my_bst.root.value)
print(my_bst.root.left.value, my_bst.root.right.value)

print(my_bst.lookup(20))
print(my_bst.lookup(5))

print(my_bst.remove(6))
print(my_bst.root.left.value)