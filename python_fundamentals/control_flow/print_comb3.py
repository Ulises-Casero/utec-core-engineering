#!/usr/bin/env python3

for num in range(10):
    for num2 in range(num + 1, 10):
        print("{:d}{:d}".format(num, num2), end=", " if num2 < 9 or num < 8 else "\n")
