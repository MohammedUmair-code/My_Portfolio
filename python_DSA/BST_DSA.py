class Node():
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 

class BinarySearchTree():
    # def __init__(self, value):
    #     new_node = Node(value)
    #     self.root = new_node 

    def __init__(self):
        self.root = None 

    def insert(self, value):
        new_node = Node(value)
        if self.root == None:
            self.root = new_node 
            return True 
        temp = self.root 
        while temp:
            if new_node.value == temp.value:
                return False 
            
            if new_node.value > temp.value:
                if temp.right != None:
                    temp = temp.right 
                else: 
                    temp.right = new_node 
            
            
            else:
                if temp.left != None:
                    temp = temp.left 
                
                else:
                    temp.left = new_node 
        return True 

    def contains(self, value):
        if self.root == None:
            return False 

        if value == self.root.value:
            return True 
        
        temp = self.root 
        while value != temp.value and temp != None:
            if value < temp.value:
                temp = temp.left
            if value > temp.value:
                temp = temp.right 
        return True 
          
            

my_tree = BinarySearchTree()
my_tree.insert(18)
my_tree.insert(16)
my_tree.insert(24)
my_tree.insert(10)
my_tree.insert(17)
my_tree.insert(20)
my_tree.insert(27)

print(my_tree.contains(10))

print(my_tree.root.value)