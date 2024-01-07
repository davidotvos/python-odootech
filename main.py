#!/usr/bin/env python3


class Auto:
    def __init__(self, id, type, doors, brand):
        self.id = id
        self.type = type
        self.doors = doors
        self.brand = brand

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, Doors: {self.doors}, Brand: {self.brand}"


class Bycicle:
    def __init__(self, id, type, load_capacity, brand):
        self.id = id
        self.type = type
        self.load_capacity = load_capacity
        self.brand = brand

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, Load capacity: {self.load_capacity}, Brand: {self.brand}"


def main():
    print("Py3")


##############################################################################

if __name__ == "__main__":
    main()
