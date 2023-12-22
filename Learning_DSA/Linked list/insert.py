
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
 # time = O(1)  space = (1)
 
 
class LinkedLIst:
    def __init__(self) :              # for empty linked list
        self.head = None
        self.tail = None              # method 2 to make a linked list 
        self.length = 0
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1 
        

n1 = LinkedLIst()
n1.append(10)
n1.append(26)
print(n1.head.value)
print(n1.length)
