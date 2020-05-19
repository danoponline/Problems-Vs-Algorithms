# Search in a Rotated Sorted Array

Binary search is used for this problem, similar to problem 1 with some modification. There are two part of input_list that has its value properly sorted from low to high, separated by the highest value. We need to know what part we are at in the while loop. Then we reset upper bound and/or lower bound appropriately until we find the solution.

# Overall Complexity
The worst-case time complexity is O(log n) for n is the length of input list. The space complexity is O(1) because we always use the same amount of memory no matter how large input.