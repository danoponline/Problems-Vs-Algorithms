def sort_012(input_list):

    # Create array of None for answer. Space complexity is O(n)
    sorted_list = [None for _ in range(len(input_list))]

    # Initialize index to keep track of zero, one, and two
    zero_tail_next = 0
    two_head_next = len(input_list) - 1
    one_head_next = len(input_list) - 1

    # Traverse in the whole input_list 1 time
    # Worst-case time complexity is O(n)
    for element in input_list:

        # Place zero in the front
        if element == 0:
            sorted_list[zero_tail_next] = element
            zero_tail_next += 1

        # Place one in the back
        elif element == 1:
            sorted_list[one_head_next] = element
            one_head_next -= 1
        
        # Place two in the back of ones
        elif element == 2:
            if sorted_list[two_head_next] is None:
                sorted_list[two_head_next] = element
                
            else:
                sorted_list[one_head_next] = sorted_list[two_head_next]
                sorted_list[two_head_next] = element
    
            two_head_next -= 1
            one_head_next -= 1

        else: # element is something else other than 0,1,2
            print("Invalid input list. List should only contain 0, 1, or 2")
            return None

    return sorted_list
        
print("Test 1: list_test = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]")

input_list = [0, 0, 2, 2, 2, 1, 1, 1, 2, 0, 2]
print(sort_012(input_list))
# Expected Output: [0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2]
print("----------------------------------------------------------------------------------------------------\n")

print("Test 2: list_test = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]")

input_list = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]
print(sort_012(input_list))
# Expected Output: [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2]
print("----------------------------------------------------------------------------------------------------\n")

print("Test 3: list_test = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1]")

input_list = [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print(sort_012(input_list))
# Expected Output: [0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2]
print("----------------------------------------------------------------------------------------------------\n")

print("Test 4: list_test = [3, 4, 5, 2, 2, 1, 1, 1, 2, 0, 2]")

input_list = [3, 4, 5, 2, 2, 1, 1, 1, 2, 0, 2]
print(sort_012(input_list))
# Expected Output: 
# Invalid input list. List should only contain 0, 1, or 2
# None
print("----------------------------------------------------------------------------------------------------\n")