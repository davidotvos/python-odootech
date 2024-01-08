#!/usr/bin/env python3

import os
import json
from pathlib import Path


class Auto:
    def __init__(self, id, type, doors, brand):
        self.id = id
        self.type = type
        self.doors = doors
        self.brand = brand

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, Doors: {self.doors}, Brand: {self.brand}"


class Bicycle:
    def __init__(self, id, type, load_capacity, brand):
        self.id = id
        self.type = type
        self.load_capacity = load_capacity
        self.brand = brand

    def __str__(self):
        return f"ID: {self.id}, Type: {self.type}, Load capacity: {self.load_capacity}, Brand: {self.brand}"


def read_data(folder_path: str) -> list:
    vehicle_list = []

    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, "r") as f:
                data = json.load(f)

                id = Path(file_path).stem

                if data["type"] == "auto":
                    vehicle = Auto(id, data["type"], data["ajtok_szama"], data["marka"])
                    vehicle_list.append(vehicle)

                elif data["type"] == "bicikli":
                    vehicle = Bicycle(
                        id, data["type"], data["terhelhetoseg"], data["marka"]
                    )
                    vehicle_list.append(vehicle)

                # Add more types if needed
                else:
                    print(data)
                    raise ValueError("Unknown transport type")

                print(f"Processing {id} - Type: {data['type']}")

    print()
    return vehicle_list


def display_data(vehicles):
    for vehicle in vehicles:
        print(vehicle)


# Example usage
def main():
    data_folder_path = "data"

    display_data(read_data(data_folder_path))


##############################################################################

if __name__ == "__main__":
    main()
