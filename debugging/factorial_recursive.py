#!/usr/bin/python3
import sys

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Check if a command-line argument is provided
if len(sys.argv) != 2:
    print("Usage: python3 script.py <number>")
    sys.exit(1)

# Try to convert the command-line argument to an integer
try:
    number = int(sys.argv[1])
except ValueError:
    print("Please provide a valid integer as input.")
    sys.exit(1)

# Calculate and print the factorial
result = factorial(number)
print(result)
