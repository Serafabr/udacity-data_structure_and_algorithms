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
    
    stack_groups = Stack()
    stack_groups.push(group)
    
    group = stack_groups.pop()
    while group:
        users = group.get_users()
        if user in users:
            return True
        sub_groups = group.get_groups()
        stack_groups.push_bulk(sub_groups)
        group = stack_groups.pop()
    
    return False


if __name__ == '__main__':
    
    parent = Group("parent")
    child = Group("child")
    sub_child = Group("subchild")

    sub_child_user = "sub_child_user"
    sub_child.add_user(sub_child_user)

    child.add_group(sub_child)
    parent.add_group(child)
    parent.add_user("normal_user")
    
    print(is_user_in_group("sub_child_user", parent))
    print(is_user_in_group("sub_child_user2", parent))
    print(is_user_in_group("normal_user", parent))
    print(is_user_in_group("normal", parent))