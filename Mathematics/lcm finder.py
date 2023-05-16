def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def lcm(numbers):
    """
    Returns the LCM of the numbers in the given list.
    """
    lcm_value = numbers[0]
    for i in range(1, len(numbers)):
        lcm_value = lcm_value * numbers[i] // gcd(lcm_value, numbers[i])
    return lcm_value

# Get the number of digits and the numbers themselves from the user
num_digits = int(input("How many numbers do you want to find the LCM of? "))
numbers = []
for i in range(num_digits):
    numbers.append(int(input("Enter number {}: ".format(i+1))))

# Call the lcm function and print the result
result = lcm(numbers)
print("The LCM of the given numbers is", result)
