class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
# node_1 = Node(3)
# print(node_1) # this will provide me the memory location

class LinkedList:
    def __init__(self, value) :
        new_node = Node(value)
        self.head = new_node          # method 1 to make a linked list 
        self.tail = new_node
        self.length = 1
        
        
# class LinkedList:
#     def __init__(self) :              # for empty linked list
#         self.head = None
#         self.tail = None              # method 2 to make a linked list 
#         self.length = 0
        
N2 = LinkedList(50)
print(N2.length)