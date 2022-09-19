# Python Lists Exercises from PYnative
# Exercises 1 - 10

# Exercise 1: Reverse a list in Python
def reverse(my_list):
    reverse_list = my_list
    # Can also do it in one line as seen below
    my_list = my_list.reverse()
    # my_list = my_list[::-1]
    return reverse_list

# Exercise 2: Concatenate two lists index wise
def zipper(list_one, list_two):
    zipped = []
    for i in range(len(list_one)):
        zipped.append(list_one[i] + list_two[i])
    # Can also do it with just one line
    # zipped = [i + j for i, j in zip(list1, list2)]
    return zipped

# Exercise 3: Square every item in a list
def squared(list):
    squares = []
    for x in list:
        squares.append(x * x)
    return squares

# Exercise 4: Concatenate two lists in a specfic order
def funky_zip(list_one, list_two):
    zipped = [i + j for i in list_one for j in list_two]
    return zipped

# Exercise 5: Iterate both lists simultaneously
# def iterate(list_one, list_two):


def print_results():
    test_list = [4,3,2,1]
    print(reverse(test_list))

    first = ["He", "lo", "wh", "w", "ca", "d"]
    second = ["re", "ok", "at", "e", "n", "o"]
    print(zipper(first, second))

    num = [1 , 2 , 3,4,5,6,7,8,9]
    print(squared(num))

    one = ["This ", "Is ", "Some "]
    two = ["Weird", "Concatenation"]
    print(funky_zip(one, two))

print_results()

