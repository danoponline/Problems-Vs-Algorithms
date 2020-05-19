def rotated_array_search(input_list, number):
    if not isinstance(number,int):
        print("Invalid number input")
        return -1
    if not isinstance(input_list,list):
        print("Invalid input_list")
        return -1
    if len(input_list) == 0 or input_list == None:
        print("Invalid input_list")
        return -1
    
    lower_bound_index = 0
    upper_bound_index = len(input_list) - 1
    
    while True:
        mid_index = (lower_bound_index + upper_bound_index) // 2
        if input_list[mid_index] == number:
            return mid_index
        
        elif lower_bound_index >= upper_bound_index:
            return -1

        # There are two part of input_list that has its value properly sorted from low to high,
        # separated by the highest value
        
        # If mid_index is a part of properly sorted upper half
        if input_list[mid_index] < input_list[upper_bound_index]:
            # If number to look for is a part of of the above condition
            if number > input_list[mid_index] and number <= input_list[upper_bound_index]:
                # Do normal binary search
                lower_bound_index = mid_index + 1
                continue

            else:
                upper_bound_index = mid_index - 1
                continue
        
        # If mid_index is a part of properly sorted lower half
        if input_list[mid_index] > input_list[lower_bound_index]:
            # If number to look for is a part of of the above condition
            if number < input_list[mid_index] and number >= input_list[lower_bound_index]:
                # Do normal binary search
                upper_bound_index = mid_index - 1
                continue
        
            else:
                lower_bound_index = mid_index + 1
                continue

print("---------------------------------------------------")
print("Test 1: list_test = [6, 7, 8, 9, 10, 1, 2, 3, 4]")
print("---------------------------------------------------")
list_test = [6, 7, 8, 9, 10, 1, 2, 3, 4]   
print(rotated_array_search(list_test, 6))
print(rotated_array_search(list_test, 1))
print(rotated_array_search(list_test, 0))
# Expected Value:
# 0
# 5
# -1
print("---------------------------------------------------")
print("Test 2: list_test = [6, 7, 8, 1, 2, 3, 4]")
print("---------------------------------------------------")
list_test = [6, 7, 8, 1, 2, 3, 4]   
print(rotated_array_search(list_test, 8))
print(rotated_array_search(list_test, 1))
print(rotated_array_search(list_test, 10))
# Expected Value:
# 2
# 3
# -1
print("---------------------------------------------------")
print("Test 3: Invalid input number or list")
print("---------------------------------------------------")
list_test = [6, 7, 8, 1, 2, 3, 4]   
print(rotated_array_search(list_test, 'a'))
print(rotated_array_search(23, 1))
print(rotated_array_search([], 1))

# Expected Value:
# Invalid number input
# -1
# Invalid input_list
# -1
# Invalid input_list
# -1
print("---------------------------------------------------")