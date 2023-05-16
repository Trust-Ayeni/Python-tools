def find_common_factors(numbers):
    """
    Returns the set of common factors of the numbers in the given list.
    """
    factors = set()
    smallest_num = min(numbers)
    
    for i in range(1, smallest_num + 1):
        if all(num % i == 0 for num in numbers):
            factors.add(i)
    
    return factors

# Get the number of digits and the numbers themselves from the user
num_digits = int(input("How many numbers do you want to find the common factors of? "))
numbers = []
for i in range(num_digits):
    numbers.append(int(input("Enter number {}: ".format(i+1))))

# Call the find_common_factors function and print the result
result = find_common_factors(numbers)
print("The common factors of the given numbers are:", result)
