# Data structure to keep subgroups and users.
class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

# Simple Stack.
# Used to keep track of what group was already checked.
class Stack():
    
    def __init__(self):
        self.arr = []
        
    def size(self):
        return len(self.arr)
    
    def is_empty(self):
        return self.size() == 0
        
    def push(self, value):
        self.arr.append(value)
        
    def push_bulk(self, values):
        self.arr = self.arr + values
    
    def pop(self):
        if self.is_empty():
            return None
        return self.arr.pop()

def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    
    # Stack of groups
    stack_groups = Stack()
    stack_groups.push(group)
    
    # Get the first group
    group = stack_groups.pop()
    
    # While there is a group on stack, keep checking
    while group:
        users = group.get_users()
        # If user was found, stop and return True
        if user in users:
            return True
        
        # Insert subgroups on stack
        sub_groups = group.get_groups()
        stack_groups.push_bulk(sub_groups)
        
        # Get the next group
        group = stack_groups.pop()
    
    return False

def test_case_01():
    # Normal case
    print('---------------------------------------')
    print("TEST CASE 01 - NORMAL CASE")
    
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_user("normal_user")
    
    print(is_user_in_group("sub_child_user", parent))
    # Answer
    # True
    print(is_user_in_group("sub_child_user2", parent))
    # Answer
    # False
    print(is_user_in_group("normal_user", parent))
    # Answer
    # True
    print(is_user_in_group("normal", parent))
    # Answer
    # False
    
    print('---------------------------------------')

def test_case_02():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 02 - EDGE CASE")
    print("Check empty group")
    
    empty_group = Group("empty_group")
    
    print(is_user_in_group("sub_child_user", empty_group))
    # Answer
    # False
    print(is_user_in_group("sub_child_user2", empty_group))
    # Answer
    # False
    print(is_user_in_group("normal_user", empty_group))
    # Answer
    # False
    print(is_user_in_group("normal", empty_group))
    # Answer
    # False
    
    print('---------------------------------------')

def test_case_03():
    # Edge case
    print('---------------------------------------')
    print("TEST CASE 03 - EDGE CASE")
    print("Large groups and subgroups")
    
    parent = Group("parent")
    
    n = 100
    for x in range(n):
        child = Group("child_" + str(x))
        child_user = "child_user_" + str(x)
        child.add_user(child_user)
        
        for y in range(n):
            subchild = Group("subchild_" + str(x) + "-" + str(y))
            subchild_user = "subchild_user_" + str(x) + "-" +  str(y)
            subchild.add_user(subchild_user)
            child.add_group(subchild)
        
        parent.add_group(child)
        parent.add_user("normal_user_" + str(x))


    
    print(is_user_in_group("sub_child_user", parent))
    # Answer
    # False
    print(is_user_in_group("subchild_user_22-42", parent))
    # Answer
    # True
    print(is_user_in_group("normal_user_33", parent))
    # Answer
    # True
    print(is_user_in_group("child_user_42", parent))
    # Answer
    # True
    print(is_user_in_group("child_user", parent))
    # Answer
    # False
    
    print('---------------------------------------')

if __name__ == '__main__':
    
    test_case_01()
    test_case_02()
    test_case_03()