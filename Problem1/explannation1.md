# Finding the Square Root of an Integer

Binary search is used for this problem. In the while loop, start with the target number. We divide the target number by 2 (integer division) and check if we reach a solution. Then we reset upper bound and lower bound and restart the while loop again until we find the solution. 

# Overall Complexity
The worst-case time complexity is O(log n) for n is an integer input number. The space complexity is O(1) because we always use the same amount of memory no matter how large input is (up to the maximum size of an int).