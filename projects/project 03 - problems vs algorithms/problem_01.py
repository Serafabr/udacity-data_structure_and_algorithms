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
    print("TEST 01 - Normal Cases")
    
    print(sqrt(9))
    print ("Pass" if  (3 == sqrt(9)) else "Fail")
    # Sqrt(9) = 3
    print(sqrt(16))
    print ("Pass" if  (4 == sqrt(16)) else "Fail")
    # Sqrt(16) = 4
    print(sqrt(1))
    print ("Pass" if  (1 == sqrt(1)) else "Fail")
    # Sqrt(1) = 1
    print(sqrt(27))
    print ("Pass" if  (5 == sqrt(27)) else "Fail")
    # Sqrt(27) = 5
    
    print("-------------------------")

def test_02():
    # Edge Cases
    # Very large numbers
    print("TEST 02 - Edge Cases  - Very large numbers")
    
    print(sqrt(40000000))
    print ("Pass" if  (6324 == sqrt(40000000)) else "Fail")
    # Sqrt(40000000) = 6324
    print(sqrt(452102099))
    print ("Pass" if  (21262 == sqrt(452102099)) else "Fail")
    # Sqrt(452102099) = 21262
    print(sqrt(124273417))
    print ("Pass" if  (11147 == sqrt(124273417)) else "Fail")
    # Sqrt(124273417) = 11147
    
    print("-------------------------")

def test_03():
    # Edge Cases
    # Negative numbers, Zero and None
    print("TEST 03 - Edge Cases - Negative numbers, Zero and None")
    
    print(sqrt(0))
    print ("Pass" if  (0 == sqrt(0)) else "Fail")
    # Sqrt(0) = 6324
    print(sqrt(-16))
    print ("Pass" if  (None == sqrt(-16)) else "Fail")
    # Sqrt(-16) = None
    print(sqrt(None))
    print ("Pass" if  (None == sqrt(None)) else "Fail")
    # Sqrt(None) = None
    
    print("-------------------------")
    
if __name__ == '__main__':
    test_01()
    test_02()
    test_03()

