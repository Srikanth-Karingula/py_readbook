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
                return (True, counter)
    print('counter:  ', counter)
    return False


def solve_OneIteration(inputList, k):
    arr_new = []*len(inputList)
    for i in range(len(inputList)):
        arr_new.append(abs(inputList[i]-k))
    print(arr_new)
    result = list(set(inputList).intersection(arr_new))
    print(result)
    if (len(result) > 0):
        print(result[0], '+', result[1], ' is ', sum_k)
        return True
    else:
        print('No combination matches')
        return False


arr = [10, 15, 3, 7, 70, 6, 2, 73, 41, 2]
sum_k = 76
result_found = 0

print(solve_input(arr, sum_k))
print(solve_OneIteration(arr, sum_k))

# Good morning! Here's your coding interview problem for today.

# This problem was asked by Jane Street.

# cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

# Given this implementation of cons:

# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair
# Implement car and cdr.


# def cons(a, b):
#     def pair(f):
#         return f(a, b)
#     return pair


# print(cons(3, 4))


# This problem was asked by Facebook.

# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.


letters = {'a': 1, 'b': 2}

print(letters['a'])
