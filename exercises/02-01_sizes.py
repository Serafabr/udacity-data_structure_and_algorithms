import sys

numbers = [1, 2123123, 3435435]
strings = ["a", "bb", "ccc", "dddd"]
floats = [1.1, 2.324, 2.5432]
mixed = [1, "a", 2.434, "dddd", "ffff", [1, 2, 3]]

print("Size of numbers is {}".format(sys.getsizeof(numbers)))
print("Size of strings is {}".format(sys.getsizeof(strings)))
print("Size of floats is {}".format(sys.getsizeof(floats)))
print("Size of mixed is {}".format(sys.getsizeof(mixed)))

print("Size inside numbers:")
for item in numbers:
    print("Size of {} is {}".format(item, sys.getsizeof(item)))
    
print("Size inside strings:")
for item in strings:
    print("Size of {} is {}".format(item, sys.getsizeof(item)))
    
print("Size inside floats:")
for item in floats:
    print("Size of {} is {}".format(item, sys.getsizeof(item)))
    
print("Size inside mixed:")
for item in mixed:
    print("Size of {} is {}".format(item, sys.getsizeof(item)))