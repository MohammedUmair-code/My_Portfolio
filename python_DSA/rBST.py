class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None 
    
class RecursiveBinarySearchTree():
    def __init__(self):
        self.root = None
    
    # def insert(self, value):
    #     new_node = Node(value)

    #     if self.root == None:
    #         self.root = new_node
    #         return True
        
    #     temp = self.root 

    #     while temp.left != None or temp.right != None and temp != None:
    #         if value == temp.value:
    #             return False
    #         if value < temp.value:
    #             temp = temp.left 
    #         if value > temp.value:
    #             temp = temp.right 
    #     temp = new_node 
    # 
    # def insert(self, value):
    #     new_node = Node(value)
    #     if self.root == None:
    #         self.root = new_node 
    #         return True 
    #     temp = self.root 
    #     while temp:
    #         if new_node.value == temp.value:
    #             return False 
            
    #         if new_node.value > temp.value:
    #             if temp.right != None:
    #                 temp = temp.right 
    #             else: 
    #                 temp.right = new_node 
            
            
    #         else:
    #             if temp.left != None:
    #                 temp = temp.left 
                
    #             else:
    #                 temp.left = new_node 
    #     return True 

    def __r_insert(self, current_node, value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
             current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.value:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node
    
    def r_insert(self, value):
        if self.root == None:
            self.root = Node(value)
        self.__r_insert(self.root, value)
    
    



    def __r_contains(self, current_node, value):
        if current_node == None:
            return False 
        if value == current_node.value:  #Is this .value actually working because the color is not right??
            return True 
        if value < current_node.value:
            return self.__r_contains(current_node.left, value)
        if value > current_node.value:
            return self.__r_contains(current_node.right, value)



    def r_contains(self, value):
        return self.__r_contains(self.root, value)
    

    def __r_delete(self, current_node, value):
        if current_node == None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left, value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right, value)
        else:
            if current_node.left == None and current_node.right == None:
                return None 
            elif current_node.left == None:
                current_node = current_node.right 
            elif current_node.right == None:
                current_node = current_node.left 
            else:
                sub_tree_min = self.min_value(current_node.right)
                current_node.value = sub_tree_min  #Why the current_node is pointing towards "sub_tree_min" and not '==' to sub_tree_min???
                current_node.right = self.__r_delete(current_node.right, sub_tree_min)

        return current_node

        
    def r_delete(self, value):
        # return self.__r_delete(self.root, value)   #Why the use of return statement is irrelevant? 
        self.root = self.__r_delete(self.root, value)  #Why self.root = is written??

    # def delete_helper(self, del_node):
    #     del_node = del_node.right 
    #     if del_node.right == None and del_node.left == None:
    #         return del_node.value

    #     if del_node.left == None:
    #         del_node.right = self.delete_helper(del_node.right)
    #     else:
    #         del_node.left = self.delete_helper(del_node.left)

    def min_value(self, current_node):
        while current_node.left != None:
            current_node = current_node.left 
        return current_node.value 
        
        


my_tree = RecursiveBinarySearchTree()

# my_rbst.r_insert(47)
# my_rbst.r_insert(21)
# my_rbst.r_insert(76)
# my_rbst.r_insert(18)
# my_rbst.r_insert(27)
# my_rbst.r_insert(52)
# my_rbst.r_insert(82)

# # print("BST Contains 27:")
# # print(my_rbst.r_contains(27))

# # print("\nBST Contains 17:")
# # print(my_rbst.r_contains(17))

# #Recursive Insert:

# # my_rbst.r_insert(2)
# # my_rbst.r_insert(1)
# # my_rbst.r_insert(3)

# # print("Root:", my_rbst.root.value)
# # print("Root -> Left:", my_rbst.root.left.value)
# # print("Root -> Right:", my_rbst.root.right.value)

# # print("\n")

# print(my_rbst.min_value(my_rbst.root))
# print(my_rbst.min_value(my_rbst.root.right))


my_tree.r_insert(2)
my_tree.r_insert(1)
my_tree.r_insert(3)

print("root:", my_tree.root.value)
print("root.left:", my_tree.root.left.value)
print("root.right:", my_tree.root.right.value)

my_tree.r_delete(2)

print("\nroot:", my_tree.root.value)
print("root.left:", my_tree.root.left.value)
print("root.right:", my_tree.root.right.value)