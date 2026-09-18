# Get a number from the user
n = int(input("Enter a number: "))

# Start with 1 because it is the identity value for multiplication
factorial = 1

# Multiply all numbers from 1 to n
for i in range(1, n + 1):
    factorial *= i

# Display the calculated factorial
print("Factorial:", factorial)
