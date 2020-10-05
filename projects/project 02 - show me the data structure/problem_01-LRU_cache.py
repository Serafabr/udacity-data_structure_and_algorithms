class Double_Node():
    
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None
        
    def set_next(self, node):
        self.next = node
    
    def set_previous(self, node):
        self.previous = node

class LRU_Cache(object):
    
    def __init__(self, capacity):
        self.recent = None
        self.
    
    def get(self, key):
        pass
    
    def set(self, key, value):
        pass
    
# Testing
our_cache = LRU_Cache(5)