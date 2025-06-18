class Node():
    def __init__(self, value):
        self.value = value 
        self.left = None 
        self.right = None 
    
class BinarySearchTree():

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


    def breadth_first_traversal(self):
        current_node = self.root 
        queue = []
        results = []
        queue.append(current_node)

        while len(queue) > 0:
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left != None:
                queue.append(current_node.left)
            if current_node.right != None:
                queue.append(current_node.right)
        return results

    def dfs_pre_order(self):
        results = []

        def traverse(current_node):
            results.append(current_node.value)
            if current_node.left != None:
                traverse(current_node.left)
            if current_node.right != None:
                traverse(current_node.right)
        traverse(self.root)
        return results

    def dfs_post_order(self):
        results = []

        def traverse_post(current_node):
            if current_node.left != None:
                traverse_post(current_node.left)
            if current_node.right != None:
                traverse_post(current_node.right)
            results.append(current_node.value)
        traverse_post(self.root)
        return results

    def dfs_in_order(self):
        results = []

        def traverse_in(current_node):
            if current_node.left != None:
                traverse_in(current_node.left)
            results.append(current_node.value
                           
                           
                           
                           
                           )
            if current_node.right != None:
                traverse_in(current_node.right)
        traverse_in(self.root)
        return results

        



my_tree = BinarySearchTree()
my_tree.insert(47)
my_tree.insert(21)
my_tree.insert(76)
my_tree.insert(18)
my_tree.insert(27)
my_tree.insert(52)
my_tree.insert(82)


print(my_tree.breadth_first_traversal()) #[47, 21, 76, 18, 27, 52, 82]
print(my_tree.dfs_pre_order())  #[47, 21, 18, 27, 76, 52, 82]
print(my_tree.dfs_post_order()) #[18, 27, 21, 52, 82, 76, 47]
print(my_tree.dfs_in_order()) #[18, 21, 27, 47, 52, 76, 82]




