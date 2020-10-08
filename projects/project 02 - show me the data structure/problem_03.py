import sys

# Node for the Huffman Tree
class Node:
    
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def has_no_children(self):
        return (self.left is None) and (self.right is None)
        
    def __str__(self):
        return "{} ({})".format(self.value, self.frequency)

class Huffman_Tree():
    
    def __init__(self):
        self.root = None
        self.code = dict({})
        
    def initialize_tree(self, priority_queue):
         #Building Tree
        node_1 = priority_queue.pop()
        node_2 = priority_queue.pop()
        
        while node_1 and node_2:
            parent_value = str(node_1.value) + str(node_2.value)
            parent_frequency = node_1.frequency + node_2.frequency 
            parent_node = Node(parent_value, parent_frequency)
            
            if node_1.frequency < node_2.frequency:
                parent_node.left = node_1
                parent_node.right = node_2
            else:
                parent_node.left = node_2
                parent_node.right = node_1
            
            priority_queue.insert(parent_node)
            
            node_1 = priority_queue.pop()
            node_2 = priority_queue.pop()
        
        # Now there's just one element on the queue
        if node_1:
            self.root = node_1
        elif node_2:
            self.root = node_2

        self.code = self._produce_code()
    
    def encode_data(self, data):
        result = ""
        for char in data:
            result += str(self.code[char]['code']) 
        return result
    
    def decode_data(self, data):
        result = ""
        node = self.root
        data_str = str(data)

        for binary in data_str:
            if binary == "0" and node.left:
                node = node.left
            elif binary == "1" and node.right:
                node = node.right
            
            if node.has_no_children():
                result += str(node.value)
                node = self.root
        
        return result
        
        
    def _produce_code(self):
        if self.root.has_no_children():
            return {self.root.value: {'freq': self.root.frequency, 'code': "1"}}
        
        leaves = {}
        self._collect_leaf_nodes(self.root, leaves)
        return leaves

    def _collect_leaf_nodes(self, node, leaves, code = ""):
        if node is not None:
            if node.has_no_children():
                "Im leaf"
                leaves[node.value] = {'freq': node.frequency, 'code': code}
            else:
                if node.left:
                    self._collect_leaf_nodes(node.left, leaves, str(code) + "0")
                if node.right:
                    self._collect_leaf_nodes(node.right, leaves, str(code) + "1")
                

# Min-heap to work as a priority queue for Node (with value, and frequency)
# PRIORITY QUEUE by frequency
class Min_Heap:
    
    def __init__(self):
        # Array starts at index 1, in order to facilitate calculations 
        self.arr = [None]
        self.num_items = 0
    
    def insert(self, node):
        self.num_items += 1
        if self.num_items >= len(self.arr):
            self.arr.append(node)
        else:
            self.arr[self.num_items] = node
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
            

def count_letters(word):
    result = dict({})
    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    return result
    
###### TODO
def generate_frequency_queue(dict_letters):
    result = Min_Heap()
    for letter, frequency in dict_letters.items():
        result.insert(Node(letter, frequency))
    
    return result

def huffman_encoding(data):
    dict_letters = count_letters(data)
    priority_queue = generate_frequency_queue(dict_letters)
    
    huffman_tree = Huffman_Tree()
    huffman_tree.initialize_tree(priority_queue)
    
    encoded_data = huffman_tree.encode_data(data)
    
    return encoded_data, huffman_tree
    


def huffman_decoding(data, tree):
    return tree.decode_data(data)

if __name__ == "__main__":
    
    a_great_sentence = "Nervously I stood there under the porch light. As you smiled at me and moved in closer. You took me in your arms, and my heart began to thud so loudly. I was sure you could hear it but were pretending you didnt. You moistened your lips, looked deeply into my eyes, And then gently pressed your lips to mine. A moment's pause, and you touched my lips with yours again, A whisper of a kiss that promised more to come. We kissed again, and during that kiss I felt like I had finally come home. Looking back, I know I was right as we kiss goodnight and I turn out the light."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))