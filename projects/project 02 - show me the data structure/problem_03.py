import sys

# Node for the Huffman Tree
class Node:
    
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
        
    def __str__(self):
        return "{} ({})".format(self.value, self.frequency)


# Min-heap to work as a priority queue
# PRIORITY QUEUE
class Min_Heap:
    
    def __init__(self):
        # Array starts at index 1, in order to facilitate calculations 
        self.arr = [None]
        self.num_items = 0
    
    def insert(self, node):
        self.arr.append(node)
        self.num_items += 1
        self._bubble_up()
    
    def pop(self):
        if self.num_items == 0:
            return None
        
        node = self.arr[1]
        self.arr[1] = self.arr[self.num_items]
        self.arr[self.num_items] = None
        self.num_items -= 1
        self._bubble_down()
        
        return node
    
    def _get_parent(self, index):
        if index <= 1:
            return None
        return index // 2
        
    def _get_left_child(self, index):
        result = index * 2
        if result > self.num_items:
            return None
        return result
        
    def _get_right_child(self, index):
        result = index * 2 + 1
        if result > self.num_items:
            return None
        return result
        
    def _is_leaf(self, index):
        return index * 2 > self.num_items
    
    def _swap_nodes(self, index_a, index_b):
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
    
    # Bubble down the first element (root)
    def _bubble_down(self):
        index = 1
        while not self._is_leaf(index):
            r_child = self._get_right_child(index)
            l_child = self._get_left_child(index)
            
            value = self.arr[index].frequency
            
            if r_child:
                r_value = self.arr[r_child].frequency
            else:
                r_value = None
            
            if l_child:
                l_value = self.arr[l_child].frequency
            else:
                l_value = None
            
            min_value = min(x for x in (value, r_value, l_value) if x is not None)
            
            if value == min_value:
                break
            
            if r_value == min_value:
                self._swap_nodes(index, r_child)
                index = r_child
            
            elif l_value == min_value:
                self._swap_nodes(index, l_child)
                index = l_child
    
    # Bubble up the last element
    def _bubble_up(self):
        index = self.num_items
        while not index == 1:
            parent = self._get_parent(index)
            
            value = self.arr[index].frequency
            p_value = self.arr[parent].frequency
            
            min_value = min(value, p_value)
            
            if p_value == min_value:
                break
            
            else:
                self._swap_nodes(index, parent)
                index = parent
    
    def __str__(self):
        output = "Priority Queue: \n"
        for value in self.arr:
            if value is not None:
                output += "{}\n".format(value)
        return output
            
    
def huffman_encoding(data):
    pass

def huffman_decoding(data,tree):
    pass

if __name__ == "__main__":
    
    # Testing Min_Heap
    priority_queue = Min_Heap()
    priority_queue.insert(Node("A", 4))
    priority_queue.insert(Node("B", 5))
    priority_queue.insert(Node("B", 2))
    priority_queue.insert(Node("B", 7))
    priority_queue.insert(Node("B", 1))
    print(priority_queue)
    print(priority_queue.pop())
    print(priority_queue)
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue.pop())
    print(priority_queue)
    
    # codes = {}

    # a_great_sentence = "The bird is the word"

    # print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # print ("The content of the data is: {}\n".format(a_great_sentence))

    # encoded_data, tree = huffman_encoding(a_great_sentence)

    # print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # print ("The content of the encoded data is: {}\n".format(encoded_data))

    # decoded_data = huffman_decoding(encoded_data, tree)

    # print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # print ("The content of the encoded data is: {}\n".format(decoded_data))