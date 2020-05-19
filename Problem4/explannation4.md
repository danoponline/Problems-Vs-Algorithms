# Dutch National Flag Problem
In this problem, we create a new list (initialized as None) of the same size as input to hold answer. We traverse the whole list one time and construct the answer. When element found is 0, we put it in the front of the answer list. When element found is 1, we put it in the back of the answer list. When element found is 2, we add 2 behind 1 and swap the last index of 1 to the front of 1. We have pointers(indices) to keep track of zero, one, and two.

# Overall Complexity
The worst-case time complexity is O(n) for n is the length of input list. The space complexity is also O(n) because we generate another list with the same length as input to hold answer.