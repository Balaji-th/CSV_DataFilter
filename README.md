# CSV_DataFilter

This project is a Python script that filters data from a marketing campaign CSV file based on customer acquisition year, month, and education level.

## Prerequisites

Before running the script, you need to have Python and the pandas library installed. You can install pandas using pip:

```bash
pip install pandas
```

## Usage

To run the script, execute the following command in your terminal:

```bash
python main.py
```

**Important Note:** The script currently has a hardcoded output path for a Windows environment. You will need to manually change the path in the `Filter_data` function in `main.py` to a suitable directory on your system. Look for the following lines and modify them accordingly:

```python
# Create directory structure for each year, month
Create_dir(f"D:\\Tasks\\Record_Filter\\Filtered_Data\\{year}\\{month}")

...

d1.to_csv(f"D:\\Tasks\\Record_Filter\\Filtered_Data\\{year}\\{month}\\{education}.csv", index=False)
```

## Dataset

The script uses the `marketing_campaign.csv` dataset, which is a tab-separated file containing customer information.

## Output

The script will create a directory named `Filtered_Data` (or the one you specify in the script) in the location you have set. Inside this directory, it will create a folder for each year, and inside each year folder, a folder for each month. The filtered data for each education level will be saved as a CSV file inside the corresponding month folder.

## Script Details

The `main.py` script contains the following functions:

*   `load_data(file_path)`: Loads the data from the CSV file.
*   `handle_missing_values(data)`: Handles missing values in the dataset.
*   `transform_data(data)`: Transforms the date column and extracts year and month.
*   `Filter_data(data)`: Filters the data and saves it to CSV files.
*   `Create_dir(nested_path)`: Creates the output directories.
