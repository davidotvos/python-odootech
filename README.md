# Vehicle Data Processor

## Overview

This Python program is designed to read and process vehicle data stored in JSON files within a specified folder. It categorizes vehicles into two types: "Auto" and "Bicycle," creating instances of corresponding classes and displaying the processed data.

## Prerequisites

- Python 3.x

## Usage

1. Clone the repository or download the `main.py` file.
2. Ensure you have Python 3.x installed on your system.
3. Run the program by executing the following command in the terminal:

```
python main.py
```
or
```
python3 main.py
```
4. The program will read JSON files from the specified folder (data by default) and display processed vehicle data.

## Data Format
The program expects JSON files with the following structure:

### Auto
```
{
  "type": "auto",
  "ajtok_szama": 4,
  "marka": "Toyota"
}
```
### Bicycle
```
{
  "type": "bicikli",
  "terhelhetoseg": 100,
  "marka": "Schwinn"
}
```
Feel free to add more types following a similar format.

## Customization
You can customize the program by modifying the `read_data` function to accommodate additional vehicle types or adjusting the data folder path.

## Example
```
# Example usage
def main():
    data_folder_path = "data"

    display_data(read_data(data_folder_path))

if __name__ == "__main__":
    main()
```

## Test
To run the tests, execute the following command in the terminal:
```
python test.py
```
or
```
python3 test.py
```
