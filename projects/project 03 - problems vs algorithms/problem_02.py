def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    start = 0
    end = len(input_list) - 1
    
    while start <= end:
        mid = (start + end) // 2
        if input_list[mid] == number:
            return mid
            
        if number <= input_list[end]:
            if input_list[mid] <= input_list[end] and number < input_list[mid]:
                end = mid - 1
            else:
                start = mid + 1
        elif number >= input_list[start]:
            if input_list[start] <= input_list[mid] and number >= input_list[mid]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            return -1
    
    return -1 

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

def test_01():
    # Normal cases
    
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
    # Answer: 0
    test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
    # Answer: 5
    test_function([[6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4], 12])
    # Answer: 6
    test_function([[6, 7, 8, 9, 10, 11, 12, 1, 2, 3, 4], 11])
    # Answer: 5
    test_function([[6, 7, 8, 1, 2, 3, 4], 8])
    # Answer: 2
    test_function([[6, 7, 8, 1, 2, 3, 4], 1])
    # Answer: 3
    test_function([[7, 8, 1, 2, 3, 4, 5, 6], 1])
    # Answer: 3
    test_function([[7, 8, 1, 2, 3, 4, 5, 6], 3])
    # Answer: 3
    test_function([[6, 7, 8, 1, 2, 3, 4], 10])
    # Answer: -1

def test_02():
    # Edge cases
    # Empty array
    
    test_function([[], 6])
    # Answer: -1

    
def test_03():
    # Edge cases
    # Large arrays
    
    arr = []
    for i in range(10000):
        arr.append(i)
    
    test_function([arr, 555])
    # Answer: 554
    test_function([arr, 50000])
    # Answer: -1
    test_function([arr, 10000])
    # Answer: 9999


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()