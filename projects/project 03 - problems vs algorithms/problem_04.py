def sort_012(input_list):
    """
    Given an input array consisting on only 0, 1, and 2, sort the array in a single traversal.

    Args:
       input_list(list): List to be sorted
    """
    next_0 = 0
    next_2 = len(input_list) - 1
    
    sorted_list = input_list[:]
    i = 0
    while i <= next_2:
        
        if sorted_list[i] == 0:
            sorted_list[i], sorted_list[next_0] = sorted_list[next_0], sorted_list[i]
            next_0 += 1
            i += 1
            
        elif sorted_list[i] == 2:
            sorted_list[i], sorted_list[next_2] = sorted_list[next_2], sorted_list[i]
            next_2 -= 1
            
        elif sorted_list[i] == 1:
            i += 1

    return sorted_list

def test_function(test_case):
    sorted_array = sort_012(test_case)
    print(sorted_array)
    if sorted_array == sorted(test_case):
        print("Pass")
    else:
        print("Fail")

# TEST CASES
def test_01():
    # Normal cases
    print("TEST 01 - Normal Cases")
    
    test_function([0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2])
    # Answer: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
    test_function([2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1])
    # Answer: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
    test_function([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2])
    # Answer: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
    
    print("-------------------------")
    

def test_02():
    # Edge cases
    # Empty list and list with one element
    print("TEST 02 - Edge Cases  - Empty list and list with one element")
    
    test_function([])
    # Answer: []
    test_function([2])
    # Answer: [2]
    test_function([0])
    # Answer: [0]
    test_function([1])
    # Answer: [1]
    
    print("-------------------------")
    
def test_03():
    # Edge cases
    # Large list
    print("TEST 03 - Edge Cases - Large lists")
    
    large_list = []
    for i in range(2, -1, -1):
        for _ in range(1000):
            large_list.append(i)
    test_function(large_list)
    # Answer: [0, ...., 1, ...., 2, ....] - 3000 elements
    
    print("-------------------------")


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()