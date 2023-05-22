def gcd(a, b):
    """
    Returns the greatest common divisor of two numbers.
    """
    while b:
        a, b = b, a % b
    return a

def find_hcf(numbers):
    """
    Returns the HCF of the numbers in the given list.
    """
    hcf_value = numbers[0]
    for i in range(1, len(numbers)):
        hcf_value = gcd(hcf_value, numbers[i])
    return hcf_value

# Get the number of digits and the numbers themselves from the user
num_digits = int(input("How many numbers do you want to find the HCF of? "))
numbers = []
for i in range(num_digits):
    numbers.append(int(input("Enter number {}: ".format(i+1))))

# Call the find_hcf function and print the result
result = find_hcf(numbers)
print("The HCF of the given numbers is", result)
