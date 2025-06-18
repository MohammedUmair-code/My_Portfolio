class Node():
    def __init__(self, value):
        self.value = value
        self.next = None 
        self.prev = None 

class DoublyLinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node 
        self.tail = new_node 
        self.length = 1

    def print_list(self):
        temp = self.head 

        while temp:
            print(temp.value)
            temp = temp.next
            
    def append(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node 
            self.tail = new_node 
        
        else:
            self.tail.next = new_node 
            new_node.prev = self.tail 
            self.tail = new_node
        self.length += 1 
        return True
    
    def pop(self):
        if self.length == 0:
            return None 
        
        temp = self.tail
        pre = self.head

        if self.length > 1:
            while pre != temp.prev:
                pre = pre.next 
            self.tail = pre 
            pre.next = None 
            temp.prev = None 
            

        else:
            self.head = None 
            self.tail = None 
            pre = None 
        self.length -= 1 
        return temp.value
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node 
            self.tail = new_node

        else:
            new_node.next = self.head 
            self.head.prev = new_node 
            self.head = new_node 
        self.length += 1 
        return True 
        
    def pop_first(self):
        if self.length == 0:
            return None 
        
        temp = self.head 
        after = self.tail 

        if self.length > 1:
            while after != temp.next:
                after = after.prev
        
            self.head = self.head.next 
            temp.next = None 
            after.prev = None 

        else: 
            self.head = None 
            self.tail = None 
            after = None

        self.length -= 1 
        return temp.value
    
    def get(self, index):
        if index < 0 or index >= self.length :
            return None 
        temp = self.head 
       
        for _ in range(index):
            temp = temp.next 

        return temp

    def set_value(self, index, value):
        if index < 0 or index >= self.length:
            return False

        temp = self.get(index)
        temp.value = value
        return True  
    
    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        new_node = Node(value)

        if self.length == 0:
            self.head = new_node
            self.tail = new_node 
        before = self.head
        after = self.tail 

        for _ in range(index - 1):
            before = before.next 
        
        while after != before.next:
            after = after.prev
        
        before.next = new_node
        new_node.next = after
        after.prev = new_node
        new_node.prev = before 
        self.length += 1
        return True 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None 
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        if self.length == 0:
            return None
        
        before = self.head 
        after = self.tail 
        temp = self.head

        for _ in range(index):
            temp = temp.next

        for _ in range(index - 1):
            before = before.next 
        
        while after.prev != before.next:
            before = before.prev
        
        before.next = temp.next
        temp.next = None 
        after.prev = temp.prev
        temp.prev = None
        self.length -= 1 
        return temp
    
        

        

my_doubly_linked_list = DoublyLinkedList(0)
my_doubly_linked_list.append(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
# my_doubly_linked_list.prepend(0)

my_doubly_linked_list.print_list()

print("\n")
# my_doubly_linked_list.set_value(1, 10)
# my_doubly_linked_list.print_list()  #0, 10, 2
# my_doubly_linked_list.insert(2, 10) 
# my_doubly_linked_list.print_list() #0, 1, 10, 2, 3

# my_doubly_linked_list.remove(1) #This particular call shows an error. What is the error and how to solve it?
my_doubly_linked_list.print_list() # 0, 1, 3



# print(my_doubly_linked_list.get(1))

# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())
# print(my_doubly_linked_list.pop_first())

# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
# print(my_doubly_linked_list.pop())
