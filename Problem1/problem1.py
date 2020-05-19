def sqrt(number):
    if not isinstance(number,int):
        print("Invalid number input. Please enter integer number that is more than 0")
        return None
    if number < 0:
        print("Invalid number input. Please enter integer number that is more than 0")
        return None

    lower_bound = 0
    upper_bound = number
    target = number
    while True:
        mid_value = (upper_bound + lower_bound) // 2
        if mid_value * mid_value == target:
            return mid_value
        elif mid_value * mid_value > target:
            upper_bound = mid_value - 1
        else: # mid_value * mid_value < target:
            lower_bound = mid_value
        
        # We the difference between the upper_bound and lower_bound is 1 or 0,
        # return the solution that is closest to target
        if upper_bound - lower_bound == 1:
            if upper_bound * upper_bound <= target:
                return upper_bound
            else:
                return lower_bound
        if upper_bound == lower_bound:
            return upper_bound

print("Testing 1: Non integer and negative number test")
print("----------------------------------------------------")
print(sqrt('a'))
print(sqrt(-1))
print(sqrt(1.23))
# Expected Result
# Invalid number input. Please enter integer number that is more than 0
# None
# Invalid number input. Please enter integer number that is more than 0
# None
# Invalid number input. Please enter integer number that is more than 0
# None

print("----------------------------------------------------\n")

print("Testing 2: Integer from 0 to 100")
print("----------------------------------------------------")
for i in range(101):
    print("i = {}, sqrt(i) = {}".format(i,sqrt(i)))
print("----------------------------------------------------\n")
# Expected Result 
# i = 0, sqrt(i) = 0
# i = 1, sqrt(i) = 1
# i = 2, sqrt(i) = 1
# i = 3, sqrt(i) = 1
# i = 4, sqrt(i) = 2
# i = 5, sqrt(i) = 2
# i = 6, sqrt(i) = 2
# i = 7, sqrt(i) = 2
# i = 8, sqrt(i) = 2
# i = 9, sqrt(i) = 3
# i = 10, sqrt(i) = 3
# i = 11, sqrt(i) = 3
# i = 12, sqrt(i) = 3
# i = 13, sqrt(i) = 3
# i = 14, sqrt(i) = 3
# i = 15, sqrt(i) = 3
# i = 16, sqrt(i) = 4
# i = 17, sqrt(i) = 4
# i = 18, sqrt(i) = 4
# i = 19, sqrt(i) = 4
# i = 20, sqrt(i) = 4
# i = 21, sqrt(i) = 4
# i = 22, sqrt(i) = 4
# i = 23, sqrt(i) = 4
# i = 24, sqrt(i) = 4
# i = 25, sqrt(i) = 5
# i = 26, sqrt(i) = 5
# i = 27, sqrt(i) = 5
# i = 28, sqrt(i) = 5
# i = 29, sqrt(i) = 5
# i = 30, sqrt(i) = 5
# i = 31, sqrt(i) = 5
# i = 32, sqrt(i) = 5
# i = 33, sqrt(i) = 5
# i = 34, sqrt(i) = 5
# i = 35, sqrt(i) = 5
# i = 36, sqrt(i) = 6
# i = 37, sqrt(i) = 6
# i = 38, sqrt(i) = 6
# i = 39, sqrt(i) = 6
# i = 40, sqrt(i) = 6
# i = 41, sqrt(i) = 6
# i = 42, sqrt(i) = 6
# i = 43, sqrt(i) = 6
# i = 44, sqrt(i) = 6
# i = 45, sqrt(i) = 6
# i = 46, sqrt(i) = 6
# i = 47, sqrt(i) = 6
# i = 48, sqrt(i) = 6
# i = 49, sqrt(i) = 7
# i = 50, sqrt(i) = 7
# i = 51, sqrt(i) = 7
# i = 52, sqrt(i) = 7
# i = 53, sqrt(i) = 7
# i = 54, sqrt(i) = 7
# i = 55, sqrt(i) = 7
# i = 56, sqrt(i) = 7
# i = 57, sqrt(i) = 7
# i = 58, sqrt(i) = 7
# i = 59, sqrt(i) = 7
# i = 60, sqrt(i) = 7
# i = 61, sqrt(i) = 7
# i = 62, sqrt(i) = 7
# i = 63, sqrt(i) = 7
# i = 64, sqrt(i) = 8
# i = 65, sqrt(i) = 8
# i = 66, sqrt(i) = 8
# i = 67, sqrt(i) = 8
# i = 68, sqrt(i) = 8
# i = 69, sqrt(i) = 8
# i = 70, sqrt(i) = 8
# i = 71, sqrt(i) = 8
# i = 72, sqrt(i) = 8
# i = 73, sqrt(i) = 8
# i = 74, sqrt(i) = 8
# i = 75, sqrt(i) = 8
# i = 76, sqrt(i) = 8
# i = 77, sqrt(i) = 8
# i = 78, sqrt(i) = 8
# i = 79, sqrt(i) = 8
# i = 80, sqrt(i) = 8
# i = 81, sqrt(i) = 9
# i = 82, sqrt(i) = 9
# i = 83, sqrt(i) = 9
# i = 84, sqrt(i) = 9
# i = 85, sqrt(i) = 9
# i = 86, sqrt(i) = 9
# i = 87, sqrt(i) = 9
# i = 88, sqrt(i) = 9
# i = 89, sqrt(i) = 9
# i = 90, sqrt(i) = 9
# i = 91, sqrt(i) = 9
# i = 92, sqrt(i) = 9
# i = 93, sqrt(i) = 9
# i = 94, sqrt(i) = 9
# i = 95, sqrt(i) = 9
# i = 96, sqrt(i) = 9
# i = 97, sqrt(i) = 9
# i = 98, sqrt(i) = 9
# i = 99, sqrt(i) = 9
# i = 100, sqrt(i) = 10