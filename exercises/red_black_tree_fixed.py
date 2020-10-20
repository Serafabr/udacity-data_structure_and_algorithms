class Node(object):
    def __init__(self, value, parent, color):
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent
        self.color = color
        # Mark how many times the value has been inserted
        self.repeated = 1
        
    def __repr__(self):
        print_color = 'R' if self.color == 'red' else 'B'
        return '%d%s(%d)' % (self.value, print_color, self.repeated)

def grandparent(node):
    if node.parent == None:
        return None
    return node.parent.parent

# Helper for finding the node's parent's sibling
def pibling(node):
    p = node.parent
    gp = grandparent(node)
    if gp == None:
        return None
    if p == gp.left:
        return gp.right
    if p == gp.right:
        return gp.left

class RedBlackTree(object):
    def __init__(self, root):
        self.root = Node(root, None, 'red')
        
    def __iter__(self):
        yield from self.root.__iter__()
        
    def search(self, value):
        print("Searching: ", value)
        current = self.root
        num_iterations = 0
        result = False
        while current:
            num_iterations += 1
            if current.value == value:
                result = current
                break
            
            if current.value < value:
                current = current.right
            
            elif current.value > value:
                current = current.left
        
        print("Iterations on search: ", num_iterations)
        return result
        
    def insert(self, new_val):
        new_node = self.insert_helper(self.root, new_val)
        if new_node.repeated == 1:
            self.rebalance(new_node)

    def insert_helper(self, current, new_val):
        if current.value == new_val:
            current.repeated += 1
            return current
        
        if current.value < new_val:
            if current.right:
                return self.insert_helper(current.right, new_val)
            else:
                current.right = Node(new_val, current, 'red')
                return current.right
        elif current.value > new_val:
            if current.left:
                return self.insert_helper(current.left, new_val)
            else:
                current.left = Node(new_val, current, 'red')
                return current.left

    def rebalance(self, node):
        # Case 1
        if node.parent == None:
            return
        
        # Case 2
        if node.parent.color == 'black':
            return
        
        # Case 3
        if pibling(node) and pibling(node).color == 'red':
            pibling(node).color = 'black'
            node.parent.color = 'black'
            grandparent(node).color = 'red'
            return self.rebalance(grandparent(node))
        
        gp = grandparent(node)        
        # Small change, if there is no grandparent, cases 4 and 5
        # won't apply
        if gp == None:
            return
        
        # Case 4
        if gp.left and node == gp.left.right:
            self.rotate_left(node.parent)
            node = node.left
        elif gp.right and node == gp.right.left:
            self.rotate_right(node.parent)
            node = node.right
    
        # Case 5
        p = node.parent
        gp = p.parent

        if node == p.left:
            self.rotate_right(gp)
        else:
            self.rotate_left(gp)
        p.color = 'black'
        gp.color = 'red'

    def rotate_left(self, node):
        # Save off the parent of the sub-tree we're rotating
        p = node.parent

        node_moving_up = node.right
        # After 'node' moves up, the right child will now be a left child
        node.right = node_moving_up.left

        # 'node' moves down, to being a left child
        node_moving_up.left = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        # 'node' may have been the root
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        else:
            self.root = node_moving_up
        node_moving_up.parent = p

    def rotate_right(self, node):
        p = node.parent

        node_moving_up = node.left
        node.left = node_moving_up.right

        node_moving_up.right = node
        node.parent = node_moving_up

        # Now we need to connect to the sub-tree's parent
        if p != None:
            if node == p.left:
                p.left = node_moving_up
            else:
                p.right = node_moving_up
        else:
            self.root = node_moving_up
        node_moving_up.parent = p
    

def print_tree(node, level=0):
    print('   ' * (level - 1) + '+--' * (level > 0) + '%s' % node)
    if node.left:
        print_tree(node.left, level + 1)
    if node.right:
        print_tree(node.right, level + 1)

##### TESTS

if __name__ == "__main__":
    tree = RedBlackTree(10)
    tree.insert(2)
    tree.insert(3)
    tree.insert(4)
    tree.insert(5)
    tree.insert(6)
    tree.insert(7)
    tree.insert(8)
    tree.insert(9)
    print_tree(tree.root)