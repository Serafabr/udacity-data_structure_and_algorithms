import sys

# Node for the Huffman Tree
class Node:
    
    # The Huffman Tree Node will keep the value and the frequency of the node.
    def __init__(self, value, frequency):
        self.value = value
        self.frequency = frequency
        self.left = None
        self.right = None
    
    def has_no_children(self):
        return (self.left is None) and (self.right is None)
        
    def __str__(self):
        return "{} ({})".format(self.value, self.frequency)

# Huffman_Tree structure - Full Binary Tree.
# It's a full binary tree in which each leaf of the tree correspond to some character to de encoded/decoded.
class Huffman_Tree():
    
    # Structure will keep the root of the tree and the dictionary with the current code for each character.
    def __init__(self):
        self.root = None
        self.code = dict({})
    
    # To initialize tree we need the priority_queue (min heap) with the characters and its frequencies (from lower freq. to higher)
    def initialize_tree(self, priority_queue):
        #Building Tree
        # Getting the first two nodes of priority_queue (value with lower frequency)
        node_1 = priority_queue.pop()
        node_2 = priority_queue.pop()
        
        # While there're at least 2 nodes on priority queue, add then together.
        while node_1 and node_2:
            # Creating the parent node for node_1 and node_2
            parent_value = str(node_1.value) + str(node_2.value)
            parent_frequency = node_1.frequency + node_2.frequency 
            parent_node = Node(parent_value, parent_frequency)
            
            # Check which node will be the left one (lower frequency)
            if node_1.frequency < node_2.frequency:
                parent_node.left = node_1
                parent_node.right = node_2
            else:
                parent_node.left = node_2
                parent_node.right = node_1
            
            # Put the parent node (mini Huffman Tree) back on the priority queue
            priority_queue.insert(parent_node)
            
            # Pop the next two nodes from priority queue (those with lower frequency)
            node_1 = priority_queue.pop()
            node_2 = priority_queue.pop()
        
        # Now there's just one element on the queue
        if node_1:
            self.root = node_1
        elif node_2:
            self.root = node_2

        # We have the root for the complete Huffman Tree. Generate the code for each character using
        # the Huffman Tree.
        self.code = self._produce_code()
    
    # Encode data with the code dictionary.
    def encode_data(self, data):
        result = ""
        for char in data:
            result += str(self.code[char]['code']) 
        return result
    
    # Decode data with the Huffman Tree.
    def decode_data(self, data):
        result = ""
        # Get Huffman Tree Root
        node = self.root
        data_str = str(data)

        # For each binary on the code, go to the left if it's 0 and to the right if it's 1.
        for binary in data_str:
            if binary == "0" and node.left:
                node = node.left
            elif binary == "1" and node.right:
                node = node.right
            
            # If this node has no children, that's the character we're searching for.
            if node.has_no_children():
                result += str(node.value)
                node = self.root
        
        return result
        
    # Produce code dicitionary with the binary code for each character. 
    # For instance, {'a': {code: '001', frequency: 7}, ....}
    def _produce_code(self):
        if self.root.has_no_children():
            return {self.root.value: {'freq': self.root.frequency, 'code': "1"}}
        
        leaves = {}
        self._collect_leaf_nodes(self.root, leaves)
        return leaves

    # Iterative method to collect all leaves from Huffman Tree.
    def _collect_leaf_nodes(self, node, leaves, code = ""):
        if node is not None:
            # Base case: there's no children. So, it's a leaf. Add it to the dictionary.
            if node.has_no_children():
                leaves[node.value] = {'freq': node.frequency, 'code': code}
            else:
                # Iterative cases. Go right, and after go left (to its children)
                if node.left:
                    self._collect_leaf_nodes(node.left, leaves, str(code) + "0")
                if node.right:
                    self._collect_leaf_nodes(node.right, leaves, str(code) + "1")
                

# Min-heap to work as a priority queue for Node (with value, and frequency)
# PRIORITY QUEUE by frequency
class Min_Heap:
    
    # Min Heap was implemented with an array. Since it will be Complete Binary Tree, the children of a parent at index will be
    # index * 2 (left child) and index * 2 + 1 (right child). The parent of a child at index will be (index // 2).
    def __init__(self):
        # Array starts at index 1, in order to facilitate computations 
        self.arr = [None]
        self.num_items = 0
    
    def insert(self, node):
        self.num_items += 1
        # First add the element to the end of the list.
        if self.num_items >= len(self.arr):
            self.arr.append(node)
        else:
            self.arr[self.num_items] = node
        # Bubble the element up on the tree, until it fulfill all the rules for the min heap.
        self._bubble_up()
    
    # It will pop the first element of the tree (its root).
    def pop(self):
        if self.num_items == 0:
            return None
            
        # It will pop the first element of the tree (its root).
        node = self.arr[1]
        # Now the new root will be the last element.
        self.arr[1] = self.arr[self.num_items]
        self.arr[self.num_items] = None
        self.num_items -= 1
        # Bubble the root down on the tree, until it fulfill all the rules for the min heap.
        self._bubble_down()
        
        return node
    
    # The node at index will have a parent at (index // 2)
    def _get_parent(self, index):
        if index <= 1:
            return None
        return index // 2
        
    
    # Node at index will have a left child at (index * 2)
    def _get_left_child(self, index):
        result = index * 2
        if result > self.num_items:
            return None
        return result
        
    # Node at index will have a right child at (index * 2 + 1)
    def _get_right_child(self, index):
        result = index * 2 + 1
        if result > self.num_items:
            return None
        return result
        
    # Check if it has a left child. If it doesn't have one, the node will not have any child (it's a complete binary tree).
    def _is_leaf(self, index):
        return index * 2 > self.num_items
    
    # Change two nodes (on the array)
    def _swap_nodes(self, index_a, index_b):
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
    
    # Bubble down the first element (root)
    def _bubble_down(self):
        # We just bubble down the root.
        index = 1
        
        # Go until this node become a leaf, 
        # or until it has the lower frequency between its frequency and its children frequencies (break statement).
        while not self._is_leaf(index):
            # Get children
            r_child = self._get_right_child(index)
            l_child = self._get_left_child(index)
            
            # Get frequencies
            value = self.arr[index].frequency
            if r_child:
                r_value = self.arr[r_child].frequency
            else:
                r_value = None
            
            if l_child:
                l_value = self.arr[l_child].frequency
            else:
                l_value = None
            
            # Calculate min value between frequencies.
            min_value = min(x for x in (value, r_value, l_value) if x is not None)
            
            # If min value is from the parent node, stop bubble down.
            if value == min_value:
                break
            
            # Otherwise, make the correct swap.
            if r_value == min_value:
                self._swap_nodes(index, r_child)
                index = r_child
            
            elif l_value == min_value:
                self._swap_nodes(index, l_child)
                index = l_child
    
    # Bubble up the last element
    def _bubble_up(self):
        # The last element will be bubbled up
        index = self.num_items
        
        # Bubble up until it's the root element, 
        # or until its parent has a lower frequency. 
        while not index == 1:
            parent = self._get_parent(index)
            
            # Get frequencies
            value = self.arr[index].frequency
            p_value = self.arr[parent].frequency
            
            # Get lower frequency
            min_value = min(value, p_value)
            
            # If its parent has a lower frequency, stop bubbling up.
            if p_value == min_value:
                break
            
            # Otherwise, swap nodes.
            else:
                self._swap_nodes(index, parent)
                index = parent
    
    def __str__(self):
        output = "Priority Queue: \n"
        for value in self.arr:
            if value is not None:
                output += "{}\n".format(value)
        return output
            
# Return a dictionary with the frequency of each letter.
def count_letters(word):
    result = dict({})
    for letter in word:
        result[letter] = result.get(letter, 0) + 1
    return result
    
# Generate a frequency queue with the Min_Heap
def generate_frequency_queue(dict_letters):
    result = Min_Heap()
    for letter, frequency in dict_letters.items():
        result.insert(Node(letter, frequency))
    
    return result

# Huffman encoding formula
def huffman_encoding(data):
    # Get frequency of each letter and generate the priority queue
    dict_letters = count_letters(data)
    priority_queue = generate_frequency_queue(dict_letters)
    
    # Turn the priority queue into a Huffman Tree.
    huffman_tree = Huffman_Tree()
    huffman_tree.initialize_tree(priority_queue)
    
    # Encode data with the Huffman Tree.
    encoded_data = huffman_tree.encode_data(data)
    
    return encoded_data, huffman_tree
    

# Huffman decoding formula
def huffman_decoding(data, tree):
    # Use the Huffman tree to decode the data.
    return tree.decode_data(data)

def test_case_01():
    # Normal case
    print('---------------------------------------')
    print("TEST CASE 01 - NORMAL CASE")
    print("Small sentence")
    
    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Size: 69
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    # 0011000101110100001101011111100111110011011101000101110100100100101111
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Size: 36

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Size: 69
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Answer - must be the same sentence.
    # The bird is the word
    print(decoded_data == a_great_sentence)
    # Answer - True
    print('---------------------------------------')
    

def test_case_02():
    # Edge case
    # Empty string
    print('---------------------------------------')
    print("TEST CASE 02 - EDGE CASE")
    print("Empty string")
    
    print('---------------------------------------')

def test_case_03():
    # Edge case
    # Big sentence - Using a poem
    print('---------------------------------------')
    print("TEST CASE 03 - EDGE CASE")
    print("Big sentence - Using a poem")
    
    a_great_sentence = "Nervously I stood there under the porch light. As you smiled at me and moved in closer. You took me in your arms, and my heart began to thud so loudly. I was sure you could hear it but were pretending you didnt. You moistened your lips, looked deeply into my eyes, And then gently pressed your lips to mine. A moment's pause, and you touched my lips with yours again, A whisper of a kiss that promised more to come. We kissed again, and during that kiss I felt like I had finally come home. Looking back, I know I was right as we kiss goodnight and I turn out the light."

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # Size: 619
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The content of the encoded data is: {}\n".format(encoded_data))
    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # Size: 352

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # Size: 619
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    # Answer - must be the same sentence.
    print(decoded_data == a_great_sentence)
    # Answer - True
    
    print('---------------------------------------')

if __name__ == "__main__":
    
    test_case_01()
    test_case_02()
    test_case_03()