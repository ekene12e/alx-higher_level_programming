#!/usr/bin/python3
def fizzbuzz():
    for number in range(1, 101):
        if not number % 3 and not number % 5:
            print("FizzBuzz", end=" ")
        elif not number % 3:
            print("Fizz", end=" ")
        elif not number % 5:
            print("Buzz", end=" ")
        else:
            print(number, end=" ")
