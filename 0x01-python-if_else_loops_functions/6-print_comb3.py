#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):
        print("{:02d}".format(i * 10 + j), end=", ")
        if i == 9 and j == 8:
            print("{}{}" .format(1 * 10 + j))
            print("\n")
