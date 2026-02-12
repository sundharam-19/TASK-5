from functools import reduce
def product_of_list(numbers):
    """
    Calculate the product of all numbers in the list using reduce and lambda.
    Handles empty lists by returning None.
    """
    if not isinstance(numbers, list) or not all(isinstance(x, (int, float)) for x in numbers):
        raise ValueError("Input must be a list of numbers.")
    if not numbers:  # Empty list case
        return None
    # reduce applies the lambda cumulatively to the list elements
    return reduce(lambda x, y: x * y, numbers)
# Example usage
try:
    nums = [2, 3, 4, 5]
    result = product_of_list(nums)
    if result is not None:
        print(f"Product of {nums} is: {result}")
    else:
        print("The list is empty, no product to calculate.")
except ValueError as e:
    print("Error:", e)
