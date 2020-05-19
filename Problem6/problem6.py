import random

def get_min_max(input_list):
    
    # Intermediate containers to hold max and min value
    min_value = None
    max_value = None

    # Go through elements in input_list 1 time
    for element in input_list:
        
        # Check if element is not an int
        if not isinstance(element,int):
            print("Input_list contains non integer values. Please only use integers.")
            return None, None

        # Put first element in both min and max containers
        if min_value == None and max_value == None:
            min_value = element
            max_value = element
            continue

        # Update max container if we find a bigger value
        elif element > max_value:
            max_value = element
            continue
        
        # Update min container if we find a smaller value
        elif element < min_value:
            min_value = element
            continue

    return min_value,max_value

# Testing
print("Test 1: list_test = a list containing 0 - 9")
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print(get_min_max(l))
# Expected Output: (0,9)

print("----------------------------------------------------------------------------------------------------\n")

print("Test 2: list_test = [-5, 2, 3, 9, 10, 100, 100, -302, -250, 20]")
l = [-5, 2, 3, 9, 10, 100, 100, -302, -250, 20]
print(get_min_max(l))
# Expected Output: (-302,100)

print("----------------------------------------------------------------------------------------------------\n")

print("Test 3: list_test = [-5, -5, -5, -5]")
l = [-5, -5, -5, -5]
print(get_min_max(l))
# Expected Output: (-5,-5)

print("----------------------------------------------------------------------------------------------------\n")

print("Test 4: list_test = ['a',2,3]")
l = ['a',2,3]
print(get_min_max(l))
# Expected Output: 
# Input_list contains non integer values. Please only use integers.
# (None,None)

print("----------------------------------------------------------------------------------------------------\n")