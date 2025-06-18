class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def merge(self, other_list):
        new_node = Node(0)
        current = new_node
        current.next = self.head
        mark_start = self.head
        mark_end = self.head
        while current:
            if self.head.next == None:
                self.head.next = other_list.head
            if self.head.value < other_list.head.value:
                self.head = self.head.next 
                current = current.next
            if other_list.head.value < self.head.value:
                temp = other_list.head
                other_list.head = other_list.head.next
                temp.next = self.head
                current.next = temp
                current = current.next
        
        self.head = mark_start
        self.length = 1
        
        while mark_end.next:
            mark_end = mark_end.next
            self.length += 1
        self.tail = mark_end

    def bubble_sort(self):
        if self.length == 0 or self.length == 1:
            return False
        current = self.head
        temp = current.next
        
        for _ in range(self.length, 0, -1):
            if current.value > temp.value:
                current.value, temp.value = temp.value, current.value
                temp= temp.next.next
            temp = temp.next 
            current = current.next
            
    


l1 = LinkedList(1)
l1.append(3)
l1.append(5)
l1.append(7)


l2 = LinkedList(2)
l2.append(4)
l2.append(6)
l2.append(8)

l1.merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""