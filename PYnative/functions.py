from ast import arg

# Exercise 1: Create a funciton in Python that takes name and age and prints their value
def name_and_age(name, age):
    print("Name: " + name)
    print("Age: " + str(age))

# Exercise 2: Create a function with a varaible length of arguments
def sum(*args):
    temp_sum = 0;
    for num in args:
        temp_sum += num
    return temp_sum

# Exercise 3: Return multiple values from a function
def SD(mean, SD):
    lower = mean - (2 * SD)
    higher = mean + (2 * SD)
    return lower, higher

# Exercise 4: Create a function with a default argument
def show_employee(name, salary=150000):
    print("Name: ", name, " & Salary: ", salary)

# Exercise 5: Inner/Wrapped Functions
def outer(a, b):
    def inner(a, b):
        return a + b
    inside = inner(a, b)
    return inside + 5

# Exercise 6: Create a recursive function (add 1 to 10)
def recursive(i):
    if(i < 10):
        # Calls itself while the value passed is less than 10
        return i + recursive(i + 1)
    else:
        return 10

# Exercise 7: Assign Different Name to a Function and Call It
def repeat_string(string):
    print(string)
# Can call function by new name now
new_function_name = repeat_string

# Exercise 8: Generate a Python list of all the even numbers between 4 to 30
def generate_list():
    even_list = []
    for x in range(4,30,2):
        even_list.append(x)
    # Can also do it via this way
    # print(list(range(4,30,2)))
    return even_list

def largest_item(example_list):
    largest = example_list[0]
    for item in example_list:
        if item > largest:
            largest = item
    # Or lighter way
    # print max(example_list)
    return largest

def print_results():
    name_and_age("Jacob", 22)

    result = sum(1, 2, 4, 12, 16)
    more_terms = sum(1,2,3,4,5,6,7,8,9,10,56,745)
    print(result)
    print(more_terms)

    response = SD(100, 25)
    print(response)

    show_employee("Poor Man", 1)
    show_employee("CEO")

    print(recursive(1))

    new_function_name("Repeated")

    print(generate_list())

    test_list = [1,2,3,5,6,7,8,9,10]
    print(largest_item(test_list))

# Print off all the methods
print_results()