class Node():
    def __init__(self, value):
        self.value = value 
        self.next = None 

class Queue():
    def __init__(self, value):
        new_node = Node(value)
        self.first = new_node 
        self.last = new_node 
        self.length = 1 
    
    def print_queue(self):
        temp = self.first 
        
        while temp:
            print(temp.value)
            temp = temp.next

    def enqueue(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node 
            self.last = new_node 

        else:
            self.last.next = new_node 
            self.last = new_node 
        self.length += 1 
        return True 
    
    def dequeue(self):
        if self.length == 0:
            return None 
        else:
            temp = self.first 
            self.first = self.first.next  #self.first.next = self.first is a wrong piece of code
            temp.next = None 
        self.length -= 1 
        return temp

my_queue = Queue(7)
my_queue.enqueue(11)
my_queue.enqueue(23)

my_queue.print_queue() #7, 11, 23

print("\n")

my_queue.dequeue()
my_queue.print_queue() #11, 23