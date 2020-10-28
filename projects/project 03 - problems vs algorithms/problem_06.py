def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None
    
    # Let the first value be max and min
    min_value = ints[0]
    max_value = ints[0]
   
   # Search for max and min values in a single traversal
    for item in ints:
        # Keep current min on min_value
        if item < min_value:
            min_value = item
        # Keep current max on max_value
        if item > max_value:
            max_value = item
    
    return (min_value, max_value)

## Example Test Case of Ten Integers
import random


def test_01():
    # Normal case
    
    l = [i for i in range(0, 10)]  # a list containing 0 - 9
    random.shuffle(l)
    print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
    # Answer: (0, 9)
    

def test_02():
    # Edge cases
    # List with one element
    
    l = [10]
    print ("Pass" if ((10, 10) == get_min_max(l)) else "Fail")
    # Answer: (10, 10)
    
    
def test_03():
    # Edge cases
    # List with negative and positive numbers
    
    l = [10, 20 , 30, -10, -6, -40, 60, 5, 3, 1, 4, 0]
    print ("Pass" if ((-40, 60) == get_min_max(l)) else "Fail")
    # Answer: (-40, 60)
    
    
def test_04():
    # Edge cases
    # Large list
    
    l = [i for i in range(0, 1000000)]  # a list containing 0 - 999999
    random.shuffle(l)
    print ("Pass" if ((0, 999999) == get_min_max(l)) else "Fail")
    # Answer: (0, 999999)


if __name__ == '__main__':
    test_01()
    test_02()
    test_03()
    test_04()