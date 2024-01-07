#!/usr/bin/env python3

class Auto:
    def __init__(self, id, type, doors, brand):
        self.id = id
        self.type = type
        self.doors = doors
        self.brand = brand

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, Doors: {self.doors}, Brand: {self.brand}"


def main():
    print("Py3")

##############################################################################

if __name__ == "__main__":
    main()