#!/usr/bin/python3
""""UTF-8 Validation"""


def validUTF8(data):
    """Write a method that determines if a given data set
       represents a valid UTF-8 encoding."""
    counter = 0
    for num in data:
        date = 0b10000000
        if not counter:
            while (date & num):
                counter += 1
                date >>= 1
            if counter > 4:
                return False
            if counter:
                counter -= 1
                if counter == 0:
                    return False
        elif counter > 0:
            if num >> 6 != 2:
                return False
            counter -= 1
    return not counter
