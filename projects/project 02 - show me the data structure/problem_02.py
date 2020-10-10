import os

# Stack to keep the folders to future look ups.
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
    
    # Create a stack of directories and files
    stack_dir = Stack()
    
    if not os.path.isdir(path):
        return "{} is not a directory.".format(path)
    
    if len(suffix) < 1:
        return "You must provide a suffix"
    
    if not suffix[0] == ".":
        return "Your suffix must start with '.'"
    
    # List all files and directories from root folder. Add them to the stack.
    for name in os.listdir(path):
        dir_path = os.path.join(path, name)
        stack_dir.push(dir_path)
    
    result = list()
    
    # Pop the first file/directory to be analysed.
    dir_path = stack_dir.pop()
    while dir_path:
        
        # If the path is a directory, get all sub items inside it and insert on stack.
        if os.path.isdir(dir_path):
            for name in os.listdir(dir_path):
                dir_path_tmp = os.path.join(dir_path, name)
                stack_dir.push(dir_path_tmp)
        
        # If the path is a file, check if it ends with the suffix in order to append to result.
        elif os.path.isfile(dir_path) and dir_path.endswith(suffix):
            result.append(dir_path)
        
        # Pop the next file/directory.
        dir_path = stack_dir.pop()
    
    return result



### TEST CASES

def test_case_01():
    # Normal test case
    print('---------------------------------------')
    print("TEST CASE 01 - NORMAL CASE")
    
    test_dir = "./testdir"
    print(find_files(".c", test_dir))
    # Answer:
    # ['./testdir/subdir1/a.c', './testdir/subdir5/a.c', './testdir/t1.c', './testdir/subdir3/subsubdir1/b.c']
    
    print('---------------------------------------')
    
def test_case_02():
    # Edge case
    # Directory don't exist
    print('---------------------------------------')
    print("TEST CASE 02 - EDGE CASE")
    print("Directory don't exist or suffix is incorrect")
    
    test_dir = "./test"
    print(find_files(".c", test_dir))
    # Answer:
    # ./test is not a directory.
    
    # Suffix is empty
    test_dir = "./testdir"
    print(find_files("", test_dir))
    # Answer:
    # "You must provide a suffix"
    
    # Suffix does not start with '.'
    test_dir = "./testdir"
    print(find_files("c", test_dir))
    # Answer:
    # "You must provide a suffix"
    
    print('---------------------------------------')

def test_case_03():
    # Edge case
    # Folder with a lot of subdirectories
    print('---------------------------------------')
    print("TEST CASE 03 - EDGE CASE")
    print("Folder with a lot of subdirectories")
    
    test_dir = "./many_dir"
    print(find_files(".c", test_dir))
    # Answer:
    # ['./many_dir/a2.c', './many_dir/a1.c', './many_dir/s1/ss1/d1.c', './many_dir/s1/ss35/d3.c', 
    # './many_dir/s1/ss50/d2.c', './many_dir/s1/b1.c', './many_dir/s1/b2.c', './many_dir/s1/ss20/d4.c', 
    # './many_dir/s8/ss17/f2.c', './many_dir/s8/ss10/f1.c', './many_dir/s50/e2.c', 
    # './many_dir/s50/e1.c', './many_dir/a3.c']
    
    print('---------------------------------------')

if __name__ == '__main__':
    test_case_01()
    test_case_02()
    test_case_03()

