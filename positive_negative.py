#!/usr/bin/env python3

# Created by DJ Watson
# Created on September 2019
# this program detects if the number is positive, negative or 0


def main():
    # input

    numinput = int(input("input number (integer): "))
    # process

    if numinput > 0:
        print("this number is positive!")
    elif numinput < 0:
        print("this number is negative!")
    elif numinput == 0:
        print("this number is 0")
    else:
        print("bruh")


if __name__ == "__main__":
    main()
