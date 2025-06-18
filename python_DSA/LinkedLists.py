class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList():
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self, value):
        new_node = Node(value)
        
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        
        self.tail.next = new_node
        self.tail = new_node
        self.length += 1
        return True

    def print_list(self):
        temp = self.head 

        while temp != None:         #Why while(temp.next) didnt work??
            print(temp.value)
            temp = temp.next

    def pop(self):
        temp = self.head
        pre = self.head 

        if self.length == 0:
            return None
        
        while(temp.next):
            temp = pre
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None 
            self.tail = None
        return temp            #Why do we need to return "temp"? and how does it affect the piece of code?
    
    def prepend(self, value):
        new_node = Node(value)

        if self.length == 0 :
            self.head = new_node
            self.tail = new_node

        # self.next = self.head  Q. Why this piece of code didn't work?
        # self.head = new_node

        else:
            new_node.next = self.head 
            self.head = new_node
        self.length += 1 
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None 
        
        temp = self.head
        self.head = self.head.next  #What will happen if I flip the code as self.head.next = self.head
        temp.next = None
        self.length -= 1 

        if self.length == 0:
            self.head = None 
            self.tail = None
        return temp
    
    def get(self, index):
        temp = self.head
        # count = 0

        # while temp != None:
        #     if count == index:
        #         return temp
        #     temp = temp.next
        #     count += 1  
        if index < 0 or index >= self.length :
            return None
        for _ in range(index):         # In loops , sometimes we use n as range for "for loop" and it seems it is not excluding the stopping range. and sometimes we use n+1 as range and it seems it is excluding the stopping range
            temp = temp.next
        return temp
    
    def set_value(self, index, value):  #This is more concise to code 
        temp = self.get(index)

        if temp:                 #why temp.value = value without if statement is not a good piece of code?
            temp.value = value
            return True
        return False

    # def set_value(self, index, value):
    #     if index < 0 or index >= self.length :
    #         return None 
        
    #     temp = self.head

    #     for _ in range(index):
    #         temp = temp.next
        
    #     if temp:
    #         temp.value = value   
    #         return True 
    #     return False


    
    def insert(self, index, value):
        if index < 0 or index > self.length :
            return False  #Not successful
        
        if index == 0:
            return self.prepend(value)
        
        if index == self.length:
            return self.append(value)
 
        new_node = Node(value)
        temp = self.get(index - 1)
        # temp = self.head

        # for _ in range(index - 1):
        #     temp = temp.next
        
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1 
        return True  #successful 
    
    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        
        if index == (self.length - 1):
            return self.pop()

        # temp = self.head
        # pre = self.head

        # for _ in range(index):
        #     pre = temp 
        #     temp = temp.next

        #More efficient way for this piece of code:
        pre = self.get(index - 1)
        temp = pre.next   # This is O(1) as against temp = self.get(index) which is O(n). hence, this is a clearer way to code.
        
        pre.next = temp.next
        temp.next = None
        self.length -= 1
        return temp
    
    def reverse(self):
        temp = self.head
        self.head = self.tail 
        self.tail = temp
        after = temp.next
        before = None

        for _ in range(self.length):
            after = temp.next
            temp.next = before 
            before = temp 
            temp = after 
        


        

    
my_linked_list = LinkedList(1)

my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)

my_linked_list.reverse()

my_linked_list.print_list() 





# my_linked_list.append(7)
 
# my_linked_list.set_value(1, 4) #11, 4, 23, 7

# my_linked_list.insert(1, 1)

# print(my_linked_list.get(2))

# my_linked_list.remove(1)

# my_linked_list.insert(1, 8) # 1, 8, 2, 3, 4

# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())
# print(my_linked_list.pop_first())







