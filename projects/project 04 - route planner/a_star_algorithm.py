import math

def get_distance_between_points(point_a, point_b):
    
    # Get coordinates from points
    x_a, y_a = point_a
    x_b, y_b = point_b
    
    # Find the variation on x and y (sides of the triangle)
    delta_x = x_a - x_b
    delta_y = y_a - y_b
    
    # Appy Pythagoras Theorem
    return math.sqrt(delta_x ** 2 + delta_y ** 2)


# Data Structure for fast lookups.
# Priority Queue.
class Min_Heap:
    
    def __init__(self):
        # Starts at index 01
        self.arr = [None]
        # Fast access to the data added to the min_heap (used to decrease a frequency of some data)
        # Save the index for any element on the hash table
        self.hash_table = dict()
        
    # Add a new element to the priority queue
    def push(self, element, frequency):
        # If element is already on the heap, just decrease frequency (if frequency is smaller)
        if element in self.hash_table:
            index = self.hash_table[element]
            if frequency < self.arr[index][0]:
                self.decrease_frequency(element, frequency)
            return
        
        item = (frequency, element)
        
        # Add item to the min heap
        self.arr.append(item)
        # Add item to the hash table (it is the last element, so far)
        self.hash_table[element] = len(self.arr) - 1
        # Bubble up the last element
        self._bubble_up(len(self.arr) - 1)
    
    def pop_min(self):
        # Check if heap has no element
        if len(self.arr) <= 1:
            return None
        
        # If heap has just one element
        if len(self.arr) == 2:
            # Pop the first element (min element)
            result = self.arr[1]
            # Clean the heap
            self.arr = [None]
            self.hash_table = dict()
            
            return result
        
        # Pop the first element (min element)
        result = self.arr[1]
        # Remove from the hash table
        del self.hash_table[result[1]]
        
        # Put last element at the beginning
        self.arr[1] = self.arr[-1]
        self.arr.pop()
        self.hash_table[self.arr[1][1]] = 1
        
        self._bubble_down()
        
        return result
        
    def decrease_frequency(self, element, new_frequency):
        # Get index
        index = self.hash_table[element]
        
        # New frequency must be smaller than the current frequency
        if self.arr[index][0] < new_frequency:
            return
        
        self.arr[index] = (new_frequency, element)
        self._bubble_up(index)
    
    def _swap_elements(self, element_a, element_b):
        # Index of these elements:
        index_a = self.hash_table[element_a]
        index_b = self.hash_table[element_b]
    
        # Swap elements on the heap and fix the hash table
        self.arr[index_a], self.arr[index_b] = self.arr[index_b], self.arr[index_a]
        self.hash_table[element_a] = index_b
        self.hash_table[element_b] = index_a
    
    # Get the parent
    def _parent(self, index):
        result = index // 2
        if result <= 0 or result >= len(self.arr):
            return None
        return result
    
    # Get left child
    def _left(self, index):
        result = index * 2
        if result <= 0 or result >= len(self.arr):
            return None
        return result
        
    # Get the right child
    def _right(self, index):
        result = index * 2 + 1
        if result <= 0 or result >= len(self.arr):
            return None
        return result
    
    # Heapify element up.
    def _bubble_up(self, index):
        
        # Get parent index
        parent_index = self._parent(index)
        
        # Keep swapping element, until it satisfies the heap conditions
        while index != 1 and self.arr[parent_index][0] > self.arr[index][0]:
            
            # Swap elements
            element = self.arr[index][1]
            parent_element = self.arr[parent_index][1]
            self._swap_elements(element, parent_element)
            
            # Update index
            index = parent_index
            parent_index = self._parent(index)
            
    # Heapify the root down.
    # Always bubble down from the root.
    def _bubble_down(self):
        # Start at the root
        index = 1
        right_index = self._right(index)
        left_index = self._left(index)
        
        # Keep swapping element, until it satisfies the heap conditions
        while (right_index or left_index):
            
            # Get the frequency value for the element and its children
            freq = self.arr[index][0]
            if right_index:
                right_freq = self.arr[right_index][0]
            else:
                right_freq = math.inf
            if left_index: 
                left_freq = self.arr[left_index][0]
            else:
                left_freq = math.inf
            
            # Check which one has the minimum frequency
            min_freq = min(freq, right_freq, left_freq)
            
            if min_freq == freq:
                return
            
            # Swap with its right child
            elif min_freq == right_freq:
                self._swap_elements(self.arr[right_index][1], self.arr[index][1])
                index = right_index
                right_index = self._right(index)
                left_index = self._left(index)
    
            # Swap with its left child
            elif min_freq == left_freq:
                self._swap_elements(self.arr[left_index][1], self.arr[index][1])
                index = left_index
                right_index = self._right(index)
                left_index = self._left(index)
            

def shortest_path(M, start, goal):
    if start >= len(M["intersections"]) or goal >= len(M["intersections"]) or start < 0 or goal < 0:
        return None
    # Use heap to get the current shortest path
    heap = Min_Heap()
    # Already visited elements
    visited = set()
    # Calculated distances
    distance = {n: math.inf for n in range(len(M["intersections"]))}
    # Previous node for the best path for each element.
    prev_node = dict()

    # Starting with the start element    
    heap.push((start, start), 0)
    distance[start] = 0

    # Just stop when goal is visited or when there's no more paths available.
    while goal not in visited and len(heap.arr) > 0:
        
        # Get next element (min distance)
        _, element = heap.pop_min()
        _, node = element
        
        visited.add(node)

        # Get all possibles roads
        roads = M["roads"][node]
        for next_node in roads:
            
            if next_node not in visited:
                # Distance from node to next_node
                partial_distance = get_distance_between_points(M["intersections"][node], M["intersections"][next_node])
                # Calculate real distance to the next node from start:
                total_distance = distance[node] + partial_distance
                
                if total_distance < distance[next_node]:
                    distance[next_node] = total_distance
                    prev_node[next_node] = node
                
                    # Heuristic towards goal
                    # Roughly distancy (straight line distance)
                    heuristic = get_distance_between_points(M["intersections"][next_node], M["intersections"][goal])
                    
                    # Add distance from start to goal, passing through next_node (using heuristic), to the heap
                    heap.push((node, next_node), distance[next_node] + heuristic)
   
    # Prepare array with path
    path = []
    node = goal
    while True:
        path.insert(0, node)
        if node == start:
            return path
        
        # Get previous node
        node = prev_node.get(node, None)
        
        if node is None:
            return None
            
    return path
    
def test_function():
        
    map = dict()
    map["intersections"] = {
        0: [0.7801603911549438, 0.49474860768712914],
        1: [0.5249831588690298, 0.14953665513987202],
        2: [0.8085335344099086, 0.7696330846542071],
        3: [0.2599134798656856, 0.14485659826020547],
        4: [0.7353838928272886, 0.8089961609345658],
        5: [0.09088671576431506, 0.7222846879290787],
        6: [0.313999018186756, 0.01876171413125327],
        7: [0.6824813442515916, 0.8016111783687677],
        8: [0.20128789391122526, 0.43196344222361227],
        9: [0.8551947714242674, 0.9011339078096633],
        10: [0.7581736589784409, 0.24026772497187532],
        11: [0.25311953895059136, 0.10321622277398101],
        12: [0.4813859169876731, 0.5006237737207431],
        13: [0.9112422509614865, 0.1839028760606296],
        14: [0.04580558670435442, 0.5886703168399895],
        15: [0.4582523173083307, 0.1735506267461867],
        16: [0.12939557977525573, 0.690016328140396],
        17: [0.607698913404794, 0.362322730884702],
        18: [0.719569201584275, 0.13985272363426526],
        19: [0.8860336256842246, 0.891868301175821],
        20: [0.4238357358399233, 0.026771817842421997],
        21: [0.8252497121120052, 0.9532681441921305],
        22: [0.47415009287034726, 0.7353428557575755],
        23: [0.26253385360950576, 0.9768234503830939],
        24: [0.9363713903322148, 0.13022993020357043],
        25: [0.6243437191127235, 0.21665962402659544],
        26: [0.5572917679006295, 0.2083567880838434],
        27: [0.7482655725962591, 0.12631654071213483],
        28: [0.6435799740880603, 0.5488515965193208],
        29: [0.34509802713919313, 0.8800306496459869],
        30: [0.021423673670808885, 0.4666482714834408],
        31: [0.640952694324525, 0.3232711412508066],
        32: [0.17440205342790494, 0.9528527425842739],
        33: [0.1332965908314021, 0.3996510641743197],
        34: [0.583993110207876, 0.42704536740474663],
        35: [0.3073865727705063, 0.09186645974288632],
        36: [0.740625863119245, 0.68128520136847],
        37: [0.3345284735051981, 0.6569436279895382],
        38: [0.17972981733780147, 0.999395685828547],
        39: [0.6315322816286787, 0.7311657634689946]
    }

    map["roads"] = [
        [36, 34, 31, 28, 17],
        [35, 31, 27, 26, 25, 20, 18, 17, 15, 6],
        [39, 36, 21, 19, 9, 7, 4],
        [35, 20, 15, 11, 6],
        [39, 36, 21, 19, 9, 7, 2],
        [32, 16, 14],
        [35, 20, 15, 11, 1, 3],
        [39, 36, 22, 21, 19, 9, 2, 4],
        [33, 30, 14],
        [36, 21, 19, 2, 4, 7],
        [31, 27, 26, 25, 24, 18, 17, 13],
        [35, 20, 15, 3, 6],
        [37, 34, 31, 28, 22, 17],
        [27, 24, 18, 10],
        [33, 30, 16, 5, 8],
        [35, 31, 26, 25, 20, 17, 1, 3, 6, 11],
        [37, 30, 5, 14],
        [34, 31, 28, 26, 25, 18, 0, 1, 10, 12, 15],
        [31, 27, 26, 25, 24, 1, 10, 13, 17],
        [21, 2, 4, 7, 9],
        [35, 26, 1, 3, 6, 11, 15],
        [2, 4, 7, 9, 19],
        [39, 37, 29, 7, 12],
        [38, 32, 29],
        [27, 10, 13, 18],
        [34, 31, 27, 26, 1, 10, 15, 17, 18],
        [34, 31, 27, 1, 10, 15, 17, 18, 20, 25],
        [31, 1, 10, 13, 18, 24, 25, 26],
        [39, 36, 34, 31, 0, 12, 17],
        [38, 37, 32, 22, 23],
        [33, 8, 14, 16],
        [34, 0, 1, 10, 12, 15, 17, 18, 25, 26, 27, 28],
        [38, 5, 23, 29],
        [8, 14, 30],
        [0, 12, 17, 25, 26, 28, 31],
        [1, 3, 6, 11, 15, 20],
        [39, 0, 2, 4, 7, 9, 28],
        [12, 16, 22, 29],
        [23, 29, 32],
        [2, 4, 7, 22, 28, 36]
    ]
    
    print(shortest_path(map, 33, 24))
    print(shortest_path(map, 0, 0))
    print(shortest_path(map, 5, 34))
    print(shortest_path(map, 0, 17))
    print(shortest_path(map, 8, 24))

if __name__ == '__main__':
    test_function()
