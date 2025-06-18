class MaxHeap():
    def __init__(self):
        self.heap = []
    
    def left_child(self, pt_index):
        left_child = (2 * pt_index) + 1 
        return left_child
    
    def right_child(self, pt_index):
        right_child = (2 * pt_index) + 2
        return right_child
    
    def parent_val(self, child_idx):
        parent_idx = (child_idx - 1 ) // 2 # int((child_idx - 1) / 2)
        return parent_idx
    
    def swap(self, idx1 , idx2):
        self.heap[idx1], self.heap[idx2] = self.heap[idx2], self.heap[idx1] #How does this works and swaps index??

    # def insert(self, value):   #Why this piece of code is not working??
        # self.heap.append(value)

        # if value != self.heap[0]: 
        #     pt_idx = self.parent_val(self.heap.index(value))

        #     while self.heap[pt_idx] < value or value == self.heap[0]:
        #         self.swap(self.heap.index(value), pt_idx)
        #     return True 

    def insert(self, value):
        self.heap.append(value)
        current = len(self.heap) - 1 

        while current > 0 and self.heap[self.parent_val(current)] < self.heap[current]:
            self.swap(current, self.parent_val(current))
            current = self.parent_val(current)

    # def remove(self):
    #     self.swap((len(self.heap) - 1), 0)
    #     self.heap.pop(len(self.heap) - 1)

    #     current = 0

    #     while current < (len(self.heap) - 1) and self.heap[current] < self.heap[self.left_child(current)] or self.heap[current] < self.heap[self.right_child(current)]:
    #         if self.heap[current] < self.heap[self.left_child(current)]:

    def remove(self):
        if len(self.heap) == 0:
            return None 
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()  #How does this line of code works? Basically what its doing is swap index 0 and last index and popping the value at index 0 BUT HOW??
        self._sink_down(0)
        return max_value

    # def _sink_down(self, idx): #Why this isn't a good piece of code for this method??
    #     current = idx

    #     while current < (len(self.heap) - 1):
    #         if self.heap[self.left_child(current)] > self.heap[self.heap[self.right_child(current)]]:
    #             if self.heap[current] < self.heap[self.left_child(current)]:
    #                 self.swap(current, self.left_child(current))
    #                 current = self.left_child(current)
            
    #         elif self.heap[self.left_child(current)] < self.heap[self.heap[self.right_child(current)]]:
    #             if self.heap[current] < self.heap[self.right_child(current)]:
    #                 self.swap(current, self.right_child(current))
    #                 current = self.right_child(current)

    #         else:
    #             if self.heap[current] < self.heap[self.right_child(current)]:
    #                 self.swap(current, self.right_child(current))
    #                 current = self.right_child(current)
                
    #             else:
    #                 pass
    
    def _sink_down(self, index):
        max_value = index  #Here, how index becomes a pointer and not just an parameter??

        while True:
            left_child = self.left_child(index)
            right_child = self.right_child(index)

            if left_child < len(self.heap) and self.heap[left_child] > self.heap[max_value]:    #Why self.heap[index] is not working but only self.heap[max_value] is working?
                max_value = left_child

            if right_child < len(self.heap) and self.heap[right_child] > self.heap[max_value]:
                max_value = right_child
            
            if max_value != index:
                self.swap(index, max_value)
                index = max_value
            else:
                return 
            



my_heap = MaxHeap()

my_heap.insert(95)
my_heap.insert(75)
my_heap.insert(80)
my_heap.insert(55)
my_heap.insert(60)
my_heap.insert(50)
my_heap.insert(65)

print(my_heap.heap)


my_heap.remove()
print(my_heap.heap)  #[80, 75, 65, 55, 60, 50]
