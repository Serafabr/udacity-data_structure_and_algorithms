class Double_Node():
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.previous = None
        self.next = None
        
    def set_values(self, key, value):
        self.key = key
        self.value = value
        
    def set_next(self, node):
        self.next = node
    
    def set_previous(self, node):
        self.previous = node
        
    def get_next(self):
        return self.next
    
    def get_previous(self):
        return self.previous
    
    def get_key(self):
        return self.key
        
    def get_value(self):
        return self.value
        
    def __str__(self):
        return f"Key: {self.key} - Value: {self.value}"


class LRU_Cache(object):
    
    def __init__(self, capacity):
        if capacity < 1:
            raise Exception("LRU Cache must have a capacity of at least 1.")
        
        self.recent = None
        self.least_recent = None
        self.hash_map = dict({})
        self.capacity = capacity
        self.num_elements = 0
    
    def get(self, key):
        node = self.hash_map.get(key, None)
        if node:
            self._move_node_to_recent(key)
            return node.get_value()
        
        return -1
    
    def set(self, key, value):
        node = self.hash_map.get(key, None)
        
        if node:
            self._move_node_to_recent(key)
            node.set_values(key, value)
            return 
        
        if self.num_elements >= self.capacity:
            self._remove_least_recent_node()
    
        self._add_new_node_to_ordered_list(Double_Node(key, value))
        
    def _move_node_to_recent(self, key):
        node = self.hash_map.get(key, None)
        if not node:
            return -1
        
        prev_node = node.previous
        next_node = node.next
        
        if prev_node is None:
            return
        
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
    
    def _add_new_node_to_ordered_list(self, node):
        key = node.get_key()
        
        if self.num_elements == 0:
            self.recent = node
            self.least_recent = node
        
        else:
            node.next = self.recent
            self.recent.previous = node
            self.recent = node

        
        self.hash_map[key] = node
        self.num_elements += 1
        
        return
    
    def _remove_least_recent_node(self):
        if self.num_elements <= 0:
            return
        
        key = self.least_recent.get_key()
        
        if self.num_elements == 1:
            self.recent = None
            self.least_recent = None
        
        else:
            self.least_recent.get_previous().next = None
            self.least_recent = self.least_recent.get_previous()
        
        self.num_elements -= 1
        del self.hash_map[key]
    
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

# Testing
our_cache = LRU_Cache(3)

our_cache.set(1, 11);

print("1")
print(our_cache)

our_cache.set(2, 12);

print("2")
print(our_cache)

our_cache.set(3, 13);

print("3")
print(our_cache)

our_cache.set(4, 14);

print("4")
print(our_cache)


print(our_cache.get(1))       # returns 1
print(our_cache.get(2))       # returns 2
print(our_cache.get(9))      # returns -1 because 9 is not present in the cache

print("5")
print(our_cache)

our_cache.set(4, 15)

print("6")
print(our_cache)

our_cache.set(6, 16)

print("7")
print(our_cache)

print(our_cache.get(3)) 