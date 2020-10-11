class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)

# Linked List
class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

# Get union of Linked List A and Linked List B and put it on another Linked List.
def union(llist_1, llist_2):
    # Get the unique values on llist_1, and put it on the dictionary memo_list_1 with its frequency (quantity)
    # {value: XX, quantity: YY}
    memo_list_1 = dict({})
    result = LinkedList()
    
    # Loop through all llist_1
    node = llist_1.head
    while node:
        result.append(node.value)
        # Getting frequency (quantity) of each element on llist_1
        memo_list_1[node.value] = memo_list_1.get(node.value, 0) + 1
        node = node.next
    
    # Loop through all llist_2
    node = llist_2.head
    while node:
        # If item was not in list_1, insert it on result
        if memo_list_1.get(node.value, None) is None:
            result.append(node.value)
        # If item was on list_1 and was already inserted Y times, we don't have to insert it again, until Y == 0 (eliminate intersection)
        elif memo_list_1[node.value] == 0:
            result.append(node.value)
        # If item was on list_1 and was already inserted Y times, we don't have to insert it again, until Y == 0 (eliminate intersection)
        # Just decrease Y by 1
        elif memo_list_1[node.value] > 0:
            memo_list_1[node.value] -= 1
        node = node.next
    
    return result
        

def intersection(llist_1, llist_2):
    # Get the unique values on llist_1, and put it on the dictionary memo_list_1 with its frequency (quantity)
    # {value: XX, quantity: YY}
    memo_list_1 = dict({})
    result = LinkedList()
    
    # Loop through all llist_1
    node = llist_1.head
    while node:
        # Getting frequency (quantity) of each element on llist_1
        memo_list_1[node.value] = memo_list_1.get(node.value, 0) + 1
        node = node.next
    
    # Loop through all llist_2
    node = llist_2.head
    while node:
        # If item was on list_1 Y times, we have to insert it and decrease Y by 1, until Y == 0 (just get intersection)
        if memo_list_1.get(node.value, None) and memo_list_1[node.value] > 0:
            result.append(node.value)
            memo_list_1[node.value] -= 1
        node = node.next
    
    return result


def test_case_01():
    # Normal case
    print('---------------------------------------')
    print("TEST CASE 01 - NORMAL CASE")
    
    linked_list_1 = LinkedList()
    linked_list_2 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,21]
    element_2 = [6,32,4,9,6,1,11,21,1]

    for i in element_1:
        linked_list_1.append(i)

    for i in element_2:
        linked_list_2.append(i)

    print (union(linked_list_1,linked_list_2))
    # Answer:
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 21 -> 32 -> 9 -> 1 -> 11 -> 1 -> 
    
    print (intersection(linked_list_1,linked_list_2))
    # Answer:
    # 6 -> 4 -> 6 -> 21 -> 

    print('---------------------------------------')

def test_case_02():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 02 - EDGE CASE")
    print("There's no intersection")
    
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = [3,2,4,35,6,65,6,4,3,23]
    element_2 = [1,7,8,9,11,21,1]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    # Answer:
    # 3 -> 2 -> 4 -> 35 -> 6 -> 65 -> 6 -> 4 -> 3 -> 23 -> 1 -> 7 -> 8 -> 9 -> 11 -> 21 -> 1 ->
    
    print (intersection(linked_list_3,linked_list_4))
    # Answer:
    #
    
    print('---------------------------------------')

def test_case_03():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 03 - EDGE CASE")
    print("Empty linked lists")
    
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    element_1 = []
    element_2 = []

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    # Answer:
    #
    
    print (intersection(linked_list_3,linked_list_4))
    # Answer:
    #
    
    print('---------------------------------------')


def text_case_04():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 04 - EDGE CASE")
    print("Large Lists")
    
    linked_list_3 = LinkedList()
    linked_list_4 = LinkedList()

    i = 100
    n = 1000
    element_1 = [x for x in range(i, n)]
    element_2 = [x for x in range(i + 500, n + 500)]

    for i in element_1:
        linked_list_3.append(i)

    for i in element_2:
        linked_list_4.append(i)

    print (union(linked_list_3,linked_list_4))
    # Answer:
    # 100 -> 101 -> 102 -> 103 -> 104 -> .....  -> 1496 -> 1497 -> 1498 -> 1499 -> 
    
    print (intersection(linked_list_3,linked_list_4))
    # Answer:
    # 600 -> 601 -> 602 -> ............ -> 998 -> 999 -> 
    
    print('---------------------------------------')


if __name__ == '__main__':
    
    test_case_01()
    test_case_02()
    test_case_03()
    text_case_04()