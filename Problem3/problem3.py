# Merge sort is used here to sort input_list
# Worst-case time complexity is O(n log n) and space complexity is O(n)
def mergesort(items):

    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):
    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] > right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged

# The overall worst-case time complexity is O(n log n) and space complexity
# is O(n) for this function. Complexity mostly comes from the merge sort
def rearrange_digits(input_list):
    # Checking if input_list has non integer number
    for element in input_list:
        if not isinstance(element,int):
            print("Invalid input_list. Please only use positive integers inside the input_list.")
            return None,None
        if element < 0:
            print("Invalid input_list. Please only use positive integers inside the input_list.")
            return None,None

    # Doing merge sort
    input_list = mergesort(input_list)
    
    # Initialize helper containers
    index = len(input_list) - 1
    pow1 = len(input_list) // 2 - 1
    pow2 = pow1
    num1 = 0
    num2 = 0
    
    # Going through input_list and construct answer num1 and num2
    # Worst-case time complexity is O(n) and space complexity is O(1)
    # in this while loop
    if len(input_list) % 2 == 1:
        pow1 += 1
        num1 += input_list[index]*(10**pow1)
        index -= 1
        pow1 -= 1

    while index >= 0:
        num1 += input_list[index]*(10**pow1)
        index -= 1
        pow1 -= 1
        num2 += input_list[index]*(10**pow2)
        index -= 1
        pow2 -= 1

    return num1,num2

# Testing
print("Test 1: input_list = [1,2,3,4,5]")

input_list = [1,2,3,4,5]
print(rearrange_digits(input_list))
# Expected Output: (542, 31)
print("----------------------------------------------------------------------------------------------------\n")

print("Test 2: input_list = [4, 6, 2, 5, 9, 8]")

input_list = [4, 6, 2, 5, 9, 8]
print(rearrange_digits(input_list))
# Expected Output: (964, 852)
print("----------------------------------------------------------------------------------------------------\n")

print("Test 3: input_list = ['a', 6, 2, 5, 9, 8]")

input_list = ['a', 6, 2, 5, 9, 8]
print(rearrange_digits(input_list))
# Expected Output:
# Invalid input_list. Please only use positive integers inside the input_list.
# (None, None)
print("----------------------------------------------------------------------------------------------------\n")

print("Test 4: input_list = [4, 6, 2, 5, 9, 8, 2, 5, 9, 4, 7]")

input_list = [4, 6, 2, 5, 9, 8, 2, 5, 9, 4, 7]
print(rearrange_digits(input_list))
# Expected Output: (997542, 86542)
print("----------------------------------------------------------------------------------------------------\n")

print("Test 5: input_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]")

input_list = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
print(rearrange_digits(input_list))
# Expected Output: (0, 0)
print("----------------------------------------------------------------------------------------------------\n")

print("Test 6: input_list = [-1, 2, -5, 0, 0, 0, 0, 0, 0, 0, 0]")

input_list = [-1, 2, -5, 0, 0, 0, 0, 0, 0, 0, 0]
print(rearrange_digits(input_list))
# Expected Output:
# Invalid input_list. Please only use positive integers inside the input_list.
# (None, None)
print("----------------------------------------------------------------------------------------------------\n")