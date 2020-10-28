# Finding the square root of an integer

def sqrt(number):
    """
    Calculate the floored square root of a number

    Args:
       number(int): Number to find the floored squared root
    Returns:
       int: Floored Square Root
    """
    if number is None or number < 0:
        return None
    
    start = 0
    end = number
    
    while start <= end:
        mid = (start + end) // 2
        square = mid * mid
        if square == number:
            return mid
        
        if square > number:
            end = mid - 1
        elif square < number:
            start = mid + 1
    return start - 1

# Tests
def test_01():
    # Normal Cases
    
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    # Sqrt(9) = 3
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    # Sqrt(16) = 4
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    # Sqrt(1) = 1
    print ("Pass" if  (5 == sqrt(27)) else "Fail")
    # Sqrt(27) = 5

def test_02():
    # Edge Cases
    # Very large numbers
    
    print ("Pass" if  (6324 == sqrt(40000000)) else "Fail")
    # Sqrt(40000000) = 6324
    print ("Pass" if  (21262 == sqrt(452102099)) else "Fail")
    # Sqrt(452102099) = 21262
    print ("Pass" if  (11147 == sqrt(124273417)) else "Fail")
    # Sqrt(124273417) = 11147

def test_03():
    # Edge Cases
    # Negative numbers, Zero and None
    
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    # Sqrt(0) = 6324
    print ("Pass" if  (None == sqrt(-16)) else "Fail")
    # Sqrt(-16) = None
    print ("Pass" if  (None == sqrt(None)) else "Fail")
    # Sqrt(None) = None
    
if __name__ == '__main__':
    test_01()
    test_02()
    test_03()

