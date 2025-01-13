#!/usr/bin/python3
""" FizzBuzz
"""
import sys


def fizzbuzz(n):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.

    - For multiples of three, print "Fizz".
    - For multiples of five, print "Buzz".
    - If a number is a multiple of both three and five, print only "Fizz" or "Buzz",
      depending on the priority (Fizz for 3, Buzz for 5).
    """
    if n < 1:
        return

    tmp_result = []
    for i in range(1, n + 1):
        if (i % 3 == 0):
            tmp_result.append("Fizz")
        elif (i % 5 == 0):
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
