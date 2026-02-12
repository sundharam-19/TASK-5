# Sample input list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# List comprehension with lambda to check even numbers and square them
squares_of_even = [x**2 for x in numbers if (lambda n: n % 2 == 0)(x)]
print(squares_of_even)
