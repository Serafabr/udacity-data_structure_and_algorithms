
# Double Node to create a Double Linked List. 
class Double_Node():
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
        
    def set_values(self, key, value):
        self.key = key
        self.value = value
    
    def get_key(self):
        return self.key
        
    def get_value(self):
        return self.value
        
    def __str__(self):
        return f"Key: {self.key} - Value: {self.value}"

# Implementation for LRU_Cache
# Implemented with a Hash Table (dictionary) and with a Double Linked List.
class LRU_Cache(object):
    
    def __init__(self, capacity = 5):
        # Capacity for LRU Cache must be at least 1.
        # There no sense in creating a cache with capacity 0 or negative.
        if capacity < 1:
            raise Exception("LRU Cache must have a capacity of at least 1.")
        
        # As it's a Double Linked List, keep tail (least_recent) and head (recent)
        self.recent = None
        self.least_recent = None
        self.hash_map = dict({})
        self.capacity = capacity
        self.num_elements = 0
    
    # Get value for certain key.
    def get(self, key):
        # Use Hash Table for searching the node. O(1)
        node = self.hash_map.get(key, None)
        # If node was found, move it to the most recent position in LRU Cache and get value.
        if node:
            self._move_node_to_recent(key)
            return node.get_value()
        
        # Cache miss.
        return -1
    
    # Insert a new value on LRU Cache.
    def set(self, key, value):
        # Check if node already exists.
        node = self.hash_map.get(key, None)
        
        # If it exists, just set its value to the current value and move the node the most recent position.
        if node:
            self._move_node_to_recent(key)
            node.set_values(key, value)
            return 
        
        # Check if it will be necessary to remove the least recent node.
        if self.num_elements >= self.capacity:
            self._remove_least_recent_node()
    
        self._add_new_node(Double_Node(key, value))
    
    # Move node to the most recent position on LRU Cache.
    def _move_node_to_recent(self, key):
        # Find node through Hash Table
        node = self.hash_map.get(key, None)
        if not node:
            return -1
        
        prev_node = node.previous
        next_node = node.next
        
        # If node is in the recent position, there will be no prev_node.
        # Do nothing.
        if prev_node is None:
            return
        
        # Move node
        elif next_node is None:
            prev_node.next = None
            self.least_recent = prev_node
        else:
            prev_node.next = next_node
            next_node.previous = prev_node
        
        node.next = self.recent
        self.recent.previous = node
        node.previous = None
        self.recent = node
        
        return
    
    # Add new node on LRU Cache
    def _add_new_node(self, node):
        # Get key from node
        key = node.get_key()
        
        # If this will be the only element on LRU Cache, it will be the most recent and the least recent.
        if self.num_elements == 0:
            self.recent = node
            self.least_recent = node
        
        # Otherwise, it will be the most recent element no LRU Cache.
        else:
            node.next = self.recent
            self.recent.previous = node
            self.recent = node

        # Save the new node on the Hash Table.
        self.hash_map[key] = node
        self.num_elements += 1
        
        return
    
    # Remove the least recent node
    def _remove_least_recent_node(self):
        # If there's no element, there will be no removal.
        if self.num_elements <= 0:
            return
        
        # Get key
        key = self.least_recent.get_key()
        
        # If it's the only element, recent and least recent will point to None.
        if self.num_elements == 1:
            self.recent = None
            self.least_recent = None
        # Otherwise, set the least recent to its previous element.
        else:
            self.least_recent.previous.next = None
            self.least_recent = self.least_recent.previous
        
        self.num_elements -= 1
        # Delete element from Hash Table
        del self.hash_map[key]
    
    # Print function
    def __str__(self):
        output = "Printing LRU Cache in order: \n"
        output += "--------------------\n"
        output += f"Recent ({self.recent}) \n"
        
        node = self.recent
        while node:
            output += f"{str(node)} - (Prev: {str(node.previous)} - Next: {str(node.next)}) \n"
            node = node.next
            
        output += f"Least Recent ({self.least_recent}) \n"
        output += "--------------------\n"
        
        return output



def test_case_01():
    
    # CASE 01 - Normal case
    print('---------------------------------------')
    print("TEST CASE 01 - NORMAL CASE")
    
    
    our_cache = LRU_Cache(5)
    our_cache.set(1, 11)
    our_cache.set(2, 12)
    our_cache.set(3, 13)
    our_cache.set(4, 14)

    print("LRU Cache after inserting: (1, 11), (2, 12), (3, 13), (4, 14)")
    print(our_cache)
    # Right answer:
    # ------------------------
    # Recent
    # Key: 4 - Value: 14
    # Key: 3 - Value: 13
    # Key: 2 - Value: 12
    # Key: 1 - Value: 11
    # Least Recent
    # ------------------------

    print("Getting values for 1, 2 and 9")
    print(our_cache.get(1))       # returns 11
    print(our_cache.get(2))       # returns 12
    print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

    print("New order of cache after getting values")
    print(our_cache)
    # Right answer:
    # ------------------------
    # Recent
    # Key: 2 - Value: 12
    # Key: 1 - Value: 11
    # Key: 4 - Value: 14
    # Key: 3 - Value: 13
    # Least Recent
    # ------------------------

    our_cache.set(5, 15)
    our_cache.set(6, 16)
    our_cache.set(7, 17)

    print("LRU Cache after inserting: (5, 15), (6, 16), (7, 17)")
    print(our_cache)
    # Right answer:
    # ------------------------
    # Recent
    # Key: 7 - Value: 17
    # Key: 6 - Value: 16
    # Key: 5 - Value: 15
    # Key: 2 - Value: 12
    # Key: 1 - Value: 11
    # Least Recent
    # ------------------------

    print("Getting values for 1, 2 and 3")
    print(our_cache.get(1))     # returns 11
    print(our_cache.get(2))     # returns 12
    print(our_cache.get(3))     # returns -1 because 3 is not present in the cache
    
    print("New order of cache after getting values")
    print(our_cache)
    # Right answer:
    # ------------------------
    # Recent
    # Key: 7 - Value: 17
    # Key: 6 - Value: 16
    # Key: 5 - Value: 15
    # Key: 2 - Value: 12
    # Key: 1 - Value: 11
    # Least Recent
    # ------------------------
    
    print('---------------------------------------')

def test_case_02():
    
    # CASE 02 - Edge case - Cache of capacity 0 or negative
    print('---------------------------------------')
    print("TEST CASE 02 - EDGE CASE")
    print("Cache of capacity 0 or negative")
    
    try:
        our_cache = LRU_Cache(-1)
        print(our_cache)
    except:
        print("Capacity should not be negative")
    
    # print Capacity should not be negative
    
    try:
        our_cache = LRU_Cache(0)
        print(our_cache)
    except:
        print("Capacity should not be 0")

    # print "Capacity should not be 0"
    
    print('---------------------------------------')

def test_case_03():
    
    # CASE 03 - Edge case - Cache with a very large capacity
    print('---------------------------------------')
    print("TEST CASE 03 - EDGE CASE")
    print("Cache with a very large capacity")
    
    size = 1000000
    our_cache = LRU_Cache(size)
    
    # Set values for the cache
    for n in range(size):
        our_cache.set(n, "Value-" + str(n))

    print("Getting values for -10, 0, 954, 55625, 545258, 999999, 1000000")
    print(our_cache.get(-10))     # returns -1 because -10 is not present in the cache
    print(our_cache.get(0))     # returns Value-0
    print(our_cache.get(954))     # returns Value-954
    print(our_cache.get(55625))     # returns Value-55625
    print(our_cache.get(545258))     # returns Value-545258
    print(our_cache.get(999999))     # returns Value-999999
    print(our_cache.get(1000000))     # returns -1 because 1000000 is not present in the cache
    
    # Set new values
    for n in range(size, size*2, 2):
        our_cache.set(n, "Value-" + str(n))
    
    
    print("Getting values for 5, 954, 55625, 1000002, 1020002, 2000000")
    print(our_cache.get(5))     # returns -1 because 5 is not present in the cache anymore
    print(our_cache.get(954))     # returns Value-954
    print(our_cache.get(55625))     # returns Value-55625
    print(our_cache.get(1000002))     # returns Value-1000002
    print(our_cache.get(1020002))     # returns Value-1020002
    print(our_cache.get(2000000))     # returns -1 because 2000000 is not present in the cache
    
    print('---------------------------------------')

if __name__ == "__main__":
    test_case_01()
    test_case_02()
    test_case_03()