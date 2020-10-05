class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class LinkedList:
    def __init__(self):
        self.head = None
    
    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        
        # Move to the tail (the last node)
        node = self.head
        while node.next:
            node = node.next
        
        node.next = Node(value)
        return
    
    def to_list(self):
        result = []
        node = self.head
        
        while node:
            result.append(node.value)
            node = node.next
            
        return result
 
 
def test():
    linked = LinkedList()
    
    linked.append(1)
    linked.append(2)
    linked.append(4)
    
    print(linked.to_list())

test()