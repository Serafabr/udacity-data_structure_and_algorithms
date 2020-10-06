import os

class Stack:
    
    def __init__(self):
        self.arr = list()
        
    def size(self):
        return len(self.arr)
        
    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return None
    
    def push(self, value):
        self.arr.append(value)
        
    def __str__(self):
        output = ""
        for item in self.arr:
            output += f"{item}\n"
        return output

def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    
    stack_dir = Stack()
    
    for name in os.listdir(path):
        dir_path = os.path.join(path, name)
        stack_dir.push(dir_path)
    
    result = list()
    
    dir_path = stack_dir.pop()
    while dir_path:
        
        if os.path.isdir(dir_path):
            for name in os.listdir(dir_path):
                dir_path_tmp = os.path.join(dir_path, name)
                stack_dir.push(dir_path_tmp)
            
        elif os.path.isfile(dir_path) and dir_path.endswith(suffix):
            result.append(dir_path)
            
        dir_path = stack_dir.pop()
    
    return result



### TEST

test_dir = "./testdir"

print(find_files(".c", test_dir))