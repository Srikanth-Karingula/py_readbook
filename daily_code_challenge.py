# Good morning! Here's your coding interview problem for today.
# This problem was recently asked by Google.
# Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
# For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
# Bonus: Can you do this in one pass?

# ab, ac, ad, bc, bd, cd


def solve_input(inputList, k):
    counter = 0
    length = len(inputList)
    for i in range(length - 1):
        for j in range(i + 1, length):
            counter += 1
            x = inputList[i]
            y = inputList[j]
            if k == (x + y):
                print(x, y, ' result is ', k)
                return True
    print('counter:  ', counter)
    return False


arr = [10, 15, 3, 7, 2, 3, 41, 2]
sum_k = 33
result_found = 0

print(solve_input(arr, sum_k))
