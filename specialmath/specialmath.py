# Recursive O(2-power-num) solution.
# This method is never used by our application.
def special_math_naive(num):
    if num < 2:
        return num

    return num + special_math_naive(num - 1) + special_math_naive(num - 2)


# Dynamic Programming - Top-down solution
# Time Complexity = O(num)
# Space Complexity = O(num)
# This method is never used by our application.
def special_math_top_down(num):
    if num < 2:
        return num
    # "num + 1" because the range is [0, num]
    dic = [-1 for i in range(num+1)]
    dic[0], dic[1] = 0, 1
    return top_down_helper(num, dic)


# Helper method for special_math_top_down method
def top_down_helper(num, dic):
    # No harm in doing a sanity check
    if num < 0:
        return num
    if dic[num] < 0:
        dic[num] = num + top_down_helper(num - 1, dic) + top_down_helper(num - 2, dic)
    return dic[num]


# Dynamic Programming - Bottom-up solution
# Time Complexity = O(num)
# Space Complexity = O(1)
def special_math_bottom_up(num):
    if num < 2:
        return num

    a, b = 0, 1

    for i in range(2, num + 1):
        tmp = b
        b = i + b + a
        a = tmp

    return b


# Calculate the result if num is a positive number
def special_math(num):
    # Adding a new line to avoid the weird character on the terminal
    result = "\n"

    if num >= 0:
        res = special_math_bottom_up(num)
        result = str(res) + "\n"

    return result
