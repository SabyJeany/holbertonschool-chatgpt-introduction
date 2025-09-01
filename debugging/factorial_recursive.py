#!/usr/bin/python3
import sys

def factorial(n):
    """
    Description:
        Calculate the factorial of a non-negative integer recursively.

    Parameters:
        n (int): Number to calculate factorial (>=0)

    Returns:
        int: factorial of n
    """
    if n==0:
        return 1
    return n*factorial(n-1)

if __name__=="__main__":
    if len(sys.argv)<2:
        print("Usage: ./factorial_recursive.py <n>")
        sys.exit(1)
    print(factorial(int(sys.argv[1])))

