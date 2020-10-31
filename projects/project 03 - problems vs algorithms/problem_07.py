# A RouteTrie will store our routes and their associated handlers
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
class RouteTrieNode:
    def __init__(self, relative_path, handler):
        # Initialize the node with children as before, plus a handler
        self.relative_path = relative_path
        self.handler = handler
        self.children = dict()

    def insert(self, relative_path, handler):
        # Insert the node as before
        if relative_path not in self.children:
            self.children[relative_path] = RouteTrieNode(relative_path, handler)
    
    def set_handler(self, handler):
        self.handler = handler
    

class RouteTrie:
    def __init__(self, root_handler):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode("/", root_handler)

    def insert(self, list_path, handler):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        
        for relative_path in list_path:
            current_node.insert(relative_path, None)
            current_node = current_node.children.get(relative_path, None)
        
        if current_node:
            current_node.set_handler(handler)

    def find(self, list_path):
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match
        current_node = self.root
        
        for relative_path in list_path:
            current_node = current_node.children.get(relative_path, None)
            if current_node is None:
                return None
        
        return current_node.handler
    
# The Router class will wrap the Trie and handle 
class Router:
    def __init__(self, root_handler, not_found_handler):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route_trie = RouteTrie(root_handler)
        self.not_found_handler = not_found_handler

    def add_handler(self, path, handler):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        list_path = self.split_path(path)
        self.route_trie.insert(list_path, handler)

    def lookup(self, path):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        list_path = self.split_path(path)
        handler = self.route_trie.find(list_path)
        
        if handler is None:
            return self.not_found_handler
        else:
            return handler

    def split_path(self, path):
        # you need to split the path into parts for 
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        return [x for x in path.split("/") if x is not ""]


def test_1():
    # Normal cases
    print("TEST 01 - Normal Cases")

    # create the router and add a route
    router = Router("root handler", "not found handler") 
    router.add_handler("/home/about", "about handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))
    print("Pass" if router.lookup("/") == "root handler" else "Fail")
    # Answer: root handler
    print(router.lookup("/home"))
    print("Pass" if router.lookup("/homt") == "not found handler" else "Fail")
    # Answer: not found handler
    print(router.lookup("/home/about"))
    print("Pass" if router.lookup("/home/about") == "about handler" else "Fail")
    # Answer: about handler
    print(router.lookup("/home/about/me")) 
    print("Pass" if router.lookup("/home/about/me") == "not found handler" else "Fail")
    # Answer: not found handler
    
    print("-------------------------")
    
def test_2():
    # Edge cases
    # Test trailing '/'
    print("TEST 02 - Edge Cases  - Trailing /")

    # create the router and add a route
    router = Router("root handler", "not found handler") 
    router.add_handler("/home/about", "about handler")  # add a route
    router.add_handler("/home/about/me", "me handler")  # add a route
    router.add_handler("/home/path1", "path1 handler")  # add a route
    router.add_handler("/home/path2", "path2 handler")  # add a route

    # some lookups with the expected output
    print(router.lookup("/"))
    print("Pass" if router.lookup("/") == "root handler" else "Fail")
    # Answer: root hanlder
    print(router.lookup("/home"))
    print("Pass" if router.lookup("/home") == "not found handler" else "Fail")
    # Answer: not found handler
    print(router.lookup("/home//about////"))
    print("Pass" if router.lookup("/home//about////") == "about handler" else "Fail")
    # Answer: about handler
    print(router.lookup("/home/about////me///////")) 
    print("Pass" if router.lookup("/home/about////me///////") == "me handler" else "Fail")
    # Answer: me handler
    print(router.lookup("/home/////not")) 
    print("Pass" if router.lookup("/home/////not") == "not found handler" else "Fail")
    # Answer: not found handler
    
    print("-------------------------")
    
def test_3():
    # Edge cases
    # Many paths
    print("TEST 03 - Edge Cases - Many Paths")

    # create the router and add a route
    router = Router("root handler", "not found handler") 
    
    for i in range(20):
        for j in range(20):
            for x in range(20):
                for y in range(20):
                    router.add_handler("/a{}/b{}/c{}/d{}".format(i, j, x, y), "a{}-b{}-c{}-d{} - handler".format(i, j, x, y))  # add a route
    
    # some lookups with the expected output
    print(router.lookup("/"))
    print("Pass" if router.lookup("/") == "root handler" else "Fail")
    # Answer: root hanlder
    print(router.lookup("/home"))
    print("Pass" if router.lookup("/home") == "not found handler" else "Fail")
    # Answer: not found handler
    print(router.lookup("/a13/b4/c14/d8")) 
    print("Pass" if router.lookup("/a13/b4/c14/d8") == "a13-b4-c14-d8 - handler" else "Fail")
    # Answer: a13-b4-c14-d8 - handler
    print(router.lookup("/a12/b8/c3/d11")) 
    print("Pass" if router.lookup("/a12/b8/c3/d11") == "a12-b8-c3-d11 - handler" else "Fail")
    # Answer: a12-b8-c3-d11 - handler
    
    print("-------------------------")

if __name__ == '__main__':
    test_1()
    test_2()
    test_3()