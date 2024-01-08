import unittest
import tempfile
import shutil
import os
import json
from unittest.mock import patch
from main import (
    read_data,
    Auto,
    Bicycle,
)


class TestReadData(unittest.TestCase):
    def setUp(self):
        # Create a temporary directory for testing
        self.temp_dir = tempfile.mkdtemp()

    def tearDown(self):
        # Remove the temporary directory after testing
        shutil.rmtree(self.temp_dir)

    def create_test_file(self, file_name, content):
        file_path = os.path.join(self.temp_dir, file_name)
        with open(file_path, "w") as file:
            json.dump(content, file)
        return file_path

    def test_read_data_with_auto(self):
        # Create a test file with Auto data
        file_content = {
            "type": "auto",
            "ajtok_szama": 5,
            "marka": "Opel",
        }
        file_path = self.create_test_file("auto_test.json", file_content)

        # Call the function and test the result
        result = read_data(self.temp_dir)
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], Auto))
        self.assertEqual(result[0].type, "auto")
        self.assertEqual(result[0].doors, 5)
        self.assertEqual(result[0].brand, "Opel")

    def test_read_data_with_bicycle(self):
        # Create a test file with Bicycle data
        file_content = {
            "type": "bicikli",
            "terhelhetoseg": 130,
            "marka": "Csepel",
        }
        file_path = self.create_test_file("bicycle_test.json", file_content)

        # Call the function and test the result
        result = read_data(self.temp_dir)
        self.assertEqual(len(result), 1)
        self.assertTrue(isinstance(result[0], Bicycle))
        self.assertEqual(result[0].type, "bicikli")
        self.assertEqual(result[0].load_capacity, 130)
        self.assertEqual(result[0].brand, "Csepel")

    def test_read_data_with_auto_and_bicycle(self):
        # Create a test file with Auto data
        auto_content = {
            "type": "auto",
            "ajtok_szama": 2,
            "marka": "Ferrari",
        }  # Adjust attribute names
        auto_file_path = self.create_test_file("auto_test.json", auto_content)

        # Create a test file with Bicycle data
        bicycle_content = {
            "type": "bicikli",
            "terhelhetoseg": 90,
            "marka": "Bmx",
        }  # Adjust attribute names
        bicycle_file_path = self.create_test_file("bicycle_test.json", bicycle_content)

        # Call the function and test the result
        result = read_data(self.temp_dir)

        # Verify the result for Auto
        auto_result = [vehicle for vehicle in result if isinstance(vehicle, Auto)]
        self.assertEqual(len(auto_result), 1, "Expected 1 Auto vehicle in the result.")
        self.assertEqual(
            auto_result[0].doors, 2, "Unexpected number of doors for Auto."
        )  # Adjust attribute names

        # Verify the result for Bicycle
        bicycle_result = [vehicle for vehicle in result if isinstance(vehicle, Bicycle)]
        self.assertEqual(
            len(bicycle_result), 1, "Expected 1 Bicycle vehicle in the result."
        )
        self.assertEqual(
            bicycle_result[0].load_capacity,
            90,
            "Unexpected load capacity for Bicycle.",
        )  # Adjust attribute names


if __name__ == "__main__":
    # Use the TextTestRunner to run the tests and display results
    test_loader = unittest.TestLoader()
    test_suite = test_loader.loadTestsFromTestCase(TestReadData)
    test_runner = unittest.TextTestRunner(verbosity=0)
    test_result = test_runner.run(test_suite)

    # Check if the tests were successful
    if test_result.wasSuccessful():
        print("All tests passed successfully.")
    else:
        print("Some tests failed. Please review the results.")
