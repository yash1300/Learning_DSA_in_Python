
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
 
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
        
    def __str__(self) :
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += '->'
            temp_node = temp_node.next
        return result  

n1 = LinkedLIst()
n1.append(210)
n1.append(263)
n1.append(210)
print(n1)
