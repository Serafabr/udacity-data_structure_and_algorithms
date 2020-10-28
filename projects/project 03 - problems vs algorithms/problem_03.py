def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    if len(input_list) == 0:
        return 0, 0
        
    # Sort the list
    sorted_list = merge_sort(input_list, 0, len(input_list) - 1)
    
    number_1 = ""
    number_2 = ""
    for i in range(len(sorted_list)):
        if i % 2 == 0:
            number_1 = str(sorted_list[i]) + number_1
        else:
            number_2 = str(sorted_list[i]) + number_2
    
    if number_1 == "":
        number_1 = 0
    if number_2 == "":
        number_2 = 0
    
    return int(number_1), int(number_2)

def merge_sort(input_list, start, end):
    if start >= end:
        return [input_list[start]]
    
    mid = (start + end) // 2
    
    # Sort left side
    left = merge_sort(input_list, start, mid)
    # Sort right side
    right = merge_sort(input_list, mid + 1, end)
    
    return merge_lists(left, right)
    

def merge_lists(list_1, list_2):
    result = []
    
    i = 0
    j = 0
    while i < len(list_1) and j < len(list_2):
        if list_1[i] <= list_2[j]:
            result.append(list_1[i])
            i += 1
        else:
            result.append(list_2[j])
            j += 1
            
    result += list_1[i:]
    result += list_2[j:]
    
    return result
             
def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

# TEST CASES
def test_01():
    # Normal cases
    
    test_case = [[4, 6, 2, 5, 9, 8], [964, 852]]
    test_function(test_case)
    # Answer: 964, 852
    test_case = [[1, 2, 3, 4, 5], [542, 31]]
    test_function(test_case)
    # Answer: 542, 31
    test_case = [[1, 4, 2, 6, 8, 9, 4, 2,], [9642, 8421]]
    test_function(test_case)
    # Answer: 964, 852

def test_02():
    # Edge cases
    # Empty list and list with one element
    
    test_case = [[], [0, 0]]
    test_function(test_case)
    # Answer: 0, 0
    test_case = [[4], [0, 4]]
    test_function(test_case)
    # Answer: 542, 31
    
def test_03():
    # Edge cases
    # Large list
    
    large_list = []
    for i in range(9, 0, -1):
        for _ in range(50):
            large_list.append(i)
    
    test_case = [large_list, [999999999999999999999999988888888888888888888888887777777777777777777777777666666666666666666666666655555555555555555555555554444444444444444444444444333333333333333333333333322222222222222222222222221111111111111111111111111, 999999999999999999999999988888888888888888888888887777777777777777777777777666666666666666666666666655555555555555555555555554444444444444444444444444333333333333333333333333322222222222222222222222221111111111111111111111111]]
    test_function(test_case)
    # Answer: 999999999999999999999999988888888888888888888888887777777777777777777777777666666666666666666666666655555555555555555555555554444444444444444444444444333333333333333333333333322222222222222222222222221111111111111111111111111, 999999999999999999999999988888888888888888888888887777777777777777777777777666666666666666666666666655555555555555555555555554444444444444444444444444333333333333333333333333322222222222222222222222221111111111111111111111111


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()