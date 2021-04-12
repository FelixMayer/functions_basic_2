# 1 Countdown - Create a function that accepts a number as an input. Return a new list that counts down by one, from the number (as the 0th element) down to 0 (as the last element).
def countdown(num):
    count = []
    for i in range(num, -1, -1):
        count.append(i)
    return count

x = countdown(5)
print(x)


# 2 Print and Return - Create a function that will receive a list with two numbers. Print the first value and return the second.
def print_return(num1, num2):
    print(num1)
    return num2

print_return(5, 19)


# 3 First Plus Length - Create a function that accepts a list and returns the sum of the first value in the list plus the list's length.
def first_length(x):
    answer = x[0] + len(x)
    return answer

y = first_length([1, 2, 3, 4])
print(y)


# 4 Values Greater than Second - Write a function that accepts a list and creates a new list containing only the values from the original list that are greater than its 2nd value. 
# Print how many values this is and then return the new list. If the list has less than 2 elements, have the function return False
def greater_than_second(x):
    newList = []
    if len(x) < 2:
        return False
    for i in x:
        if i > x[1]:
            newList.append(i)
    print(len(newList))
    return newList

first = greater_than_second([5,2,3,2,1,4])
print(first)
second = greater_than_second([3])
print(second)


# 5 This length, that value - Write a function that accepts two integers as parameters: size and value. 
# The function should create and return a list whose length is equal to the given size, and whose values are all the given value.
def length_value(size, value):
    newList = []
    for i in range(size):
        newList.append(value)
    return newList

a = length_value(4,7)
print(a)